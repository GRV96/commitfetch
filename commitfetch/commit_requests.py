# __all__ declared at the module's end

import json
import requests
from time import\
	sleep

from ghae import\
	GitHubApiError,\
	detect_github_api_error

from .github_data import\
	Commit,\
	GitHubCredRepository,\
	GitHubUser,\
	GitHubUserRepository,\
	RepoIdentity


_KEY_AUTHOR = "author"
_KEY_COMMIT = "commit"
_KEY_COMMITTER = "committer"
_KEY_DATE = "date"
_KEY_FILENAME = "filename"
_KEY_FILES = "files"
_KEY_ID = "id"
_KEY_LOGIN = "login"
_KEY_MESSAGE = "message"
_KEY_NAME = "name"
_KEY_SHA = "sha"
_KEY_URL = "url"

_PATH_COMMITS = "/commits/"

_PATH_REPOS = "https://api.github.com/repos/"
_PATH_REPOS_LEN = len(_PATH_REPOS)
_PATH_USERS = "https://api.github.com/users/"

_RATE_LIMIT_EXCEEDED = "API rate limit exceeded"

_STATUS_404 = "404"

_TIME_BEFORE_API_AVAILABLE = 3602 # seconds

_USER_REPO = GitHubUserRepository()


def _catch_api_rate_limit_exception(gae, credentials, can_wait):
	credential = credentials.get_next_credential()

	if credential is None:
		if can_wait:
			sleep(_TIME_BEFORE_API_AVAILABLE)
			credentials.reset_credential_iter()
			credential = credentials.get_next_credential()
		else:
			raise gae

	return credential


def _catch_github_api_error(gae, credentials, can_wait):
	if _RATE_LIMIT_EXCEEDED in gae.message:
		return _catch_api_rate_limit_exception(gae, credentials, can_wait)

	else:
		raise gae


def _get_commit_author_login_and_id(commit_data):
	author_login = None
	author_id = None

	author_struct = commit_data[_KEY_AUTHOR]
	if author_struct is not None:
		author_login = author_struct.get(_KEY_LOGIN)
		author_id = author_struct.get(_KEY_ID)

	if author_login is None:
		committer_struct = commit_data[_KEY_COMMITTER]
		if committer_struct is not None:
			author_login = committer_struct.get(_KEY_LOGIN)
			author_id = committer_struct.get(_KEY_ID)

	return author_login, author_id


def get_repo_commits(repository, credentials, can_wait):
	"""
	This generator obtains data about all the commits in a GitHub repository
	through the GitHub API. Each iteration yields data about one commit.
	
	The caller must provide GitHub credentials to authenticate the requests to
	the GitHub API. Each credential must be a tuple containing a GitHub usename
	(str, index 0) and a token owned by the corresponding user (str, index 1).

	If argument credentials is of type GitHubCredRepository, it will be used as
	is. If it is a generator, a list, a set or a tuple, its content will be
	used to create a GitHubCredRepository.

	The GitHub API allows 5000 authenticated requests per user per hour. When
	the request rate limit is exceeded, an error occurs. At that moment, if
	argument can_wait is False, this generator raises an exception. If can_wait
	is True, this generator waits for one hour then resumes sending requests.

	Parameters:
		repository (str): a repository's full name in the format
			<owner>/<name>.
		credentials: GitHub credentials.
		can_wait (bool): allows this generator to wait if the GitHub API's
			request rate limit is exceeded.

	Yields:
		Commit: data about one commit from the specified repository.

	Raises:
		GitHubApiError: if an error occurred upon a request to the GitHub API.
	"""
	cred_repo = credentials
	if not isinstance(cred_repo, GitHubCredRepository):
		cred_repo = GitHubCredRepository(credentials)

	credential = cred_repo.get_next_credential()

	page_num = 1

	# Loop through all the commit pages until an empty page is encountered.
	while True:
		try:
			commit_page_data = _request_commit_page(
				repository, page_num, credential)

		except GitHubApiError as gae:
			credential = _catch_github_api_error(gae, cred_repo, can_wait)
			continue

		commit_data_len = len(commit_page_data)
		if commit_data_len == 0:
			# Stop the loop if there are no more commits in the pages.
			break

		# Iterate through the list of commits from the page.
		commit_data_index = 0
		while commit_data_index < commit_data_len:
			commit_sha = commit_page_data[commit_data_index][_KEY_SHA]

			try:
				commit = _request_commit(commit_sha, repository, credential)
				yield commit

			except GitHubApiError as gae:
				credential = _catch_github_api_error(gae, cred_repo, can_wait)
				continue

			commit_data_index += 1

		page_num += 1


def _make_commit_from_api_data(commit_data, credential):
	sha = commit_data[_KEY_SHA]

	api_url = commit_data[_KEY_URL]
	repo_identity = _repo_from_commit_api_url(api_url)

	commit_struct = commit_data[_KEY_COMMIT]
	message = commit_struct[_KEY_MESSAGE]
	commit_author_struct = commit_struct[_KEY_AUTHOR]
	moment = commit_author_struct[_KEY_DATE]

	author = None
	author_login, author_id = _get_commit_author_login_and_id(commit_data)

	if author_login is not None:
		try:
			author = _request_github_user(author_login, credential)
		except GitHubApiError as gae:
			if gae.status != _STATUS_404:
				raise

			author = GitHubUser(author_id, author_login, None)

	file_data = commit_data[_KEY_FILES]
	file_generator = (fd[_KEY_FILENAME] for fd in file_data)

	return Commit(sha, message, repo_identity, moment, author, file_generator)


def _make_github_user_from_api_data(github_user_data):
	id = github_user_data[_KEY_ID]
	login = github_user_data[_KEY_LOGIN]
	name = github_user_data[_KEY_NAME]

	github_user = GitHubUser(id, login, name)
	_USER_REPO.register_user(github_user)

	return github_user


def _repo_from_commit_api_url(url):
	path_commits_index = url.index(_PATH_COMMITS)
	repo_full_name =  url[_PATH_REPOS_LEN: path_commits_index]
	return RepoIdentity.from_full_name(repo_full_name)


def _request_commit(commit_sha, repository, credential):
	"""
	Requests a commit from the GitHub API. The caller must provide a GitHub
	credential to authenticate the requests to the GitHub API.

	Parameters:
		commit_sha (str): a SHA hash that identifies a commit.
		repository (str): a GitHub repository name in the format
			<owner>/<name>.
		credential (tuple): a GitHub credential consisting of a username
			(str, index 0) and a PAT (str, index 1).
	
	Returns:
		Commit: an object that contains the wanted commit's data.

	Raises:
		GitHubApiError: if the response indicates that an error occurred.
	"""
	commit_url = _PATH_REPOS + repository + _PATH_COMMITS + commit_sha
	commit_response = requests.get(commit_url, auth=credential)
	commit_data = json.loads(commit_response.content)

	detect_github_api_error(commit_url, commit_data)

	try:
		commit = _make_commit_from_api_data(commit_data, credential)
	except Exception as ex:
		ex.add_note(f"Commit URL: {commit_url}")
		raise

	return commit


def _request_commit_page(repository, page_num, credential):
	"""
	Requests a page of commit data from the GitHub API. The caller must provide
	a GitHub credential to authenticate the requests to the GitHub API.

	Parameters:
		repository (str): a GitHub repository name in the format
			<owner>/<name>.
		page_num (int): the number of a commit page on the GitHub API, >= 1.
		credential (tuple): a GitHub credential consisting of a username
			(str, index 0) and a PAT (str, index 1).

	Returns:
		list: the data of the commits from the wanted page.

	Raises:
		GitHubApiError: if the response indicates that an error occurred.
	"""
	commit_page_url = _PATH_REPOS + repository\
		+ '/commits?page=' + str(page_num)
	commits_response = requests.get(commit_page_url, auth=credential)
	commit_page_data = json.loads(commits_response.content)

	detect_github_api_error(commit_page_url, commit_page_data)

	return commit_page_data


def _request_github_user(user_login, credential):
	"""
	Request data about a GitHub user from the GitHub API. The caller must
	provide a GitHub credential to authenticate the requests to the GitHub API.

	Parameters:
		user_login (str): the wanted user's login name, which corresponds to
			property GitHubUser.login.
		credential (tuple): a GitHub credential consisting of a username
			(str, index 0) and a PAT (str, index 1).

	Returns:
		GitHubUser: data about the specified GitHub user.

	Raises:
		GitHubApiError: if the response indicates that an error occurred.
	"""
	github_user = _USER_REPO.get_user(user_login)
	if github_user is not None:
		return github_user

	user_url = _PATH_USERS + user_login
	user_response = requests.get(user_url, auth=credential)
	github_user_data = json.loads(user_response.content)

	try:
		detect_github_api_error(user_url, github_user_data)
	except Exception as ex:
		ex.add_note(f"User URL: {user_url}")
		raise

	github_user = _make_github_user_from_api_data(github_user_data)
	return github_user


__all__ = [get_repo_commits.__name__]
