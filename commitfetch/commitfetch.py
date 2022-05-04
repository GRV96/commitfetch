import json
import requests
from time import sleep

from .commit import\
	Commit,\
	RepoIdentity


_KEY_AUTHOR = "author"
_KEY_COMMIT = "commit"
_KEY_DATE = "date"
_KEY_DOCUMENTATION_URL = "documentation_url"
_KEY_FILENAME = "filename"
_KEY_FILES = "files"
_KEY_MESSAGE = "message"
_KEY_NAME = "name"
_KEY_SHA = "sha"
_KEY_URL = "url"

_PATH_COMMITS = "/commits/"

_PATH_REPOS = "https://api.github.com/repos/"
_PATH_REPOS_LEN = len(_PATH_REPOS)

_RATE_LIMIT_EXCEEDED = "API rate limit exceeded"

_TIME_BEFORE_API_AVAILABLE = 3602


def _catch_api_rate_limit_exception(api_except, credentials, can_wait):
	token = credentials.get_next_token()

	if token is None:
		if can_wait:
			sleep(_TIME_BEFORE_API_AVAILABLE)
			credentials.reset_token_iter()
			token = credentials.get_next_token()
		else:
			raise api_except

	return token


def _catch_github_api_exception(api_except, credentials, can_wait):
	if _RATE_LIMIT_EXCEEDED in str(api_except):
		return _catch_api_rate_limit_exception(
			api_except, credentials, can_wait)

	else:
		raise api_except


def _commit_from_api_data(commit_data):
	sha = commit_data[_KEY_SHA]

	api_url = commit_data[_KEY_URL]
	repo_identity = _repo_from_commit_api_url(api_url)

	commit_struct = commit_data[_KEY_COMMIT]
	message = commit_struct[_KEY_MESSAGE]

	author_struct = commit_struct[_KEY_AUTHOR]
	author = author_struct[_KEY_NAME]
	moment = author_struct[_KEY_DATE]

	file_data = commit_data[_KEY_FILES]
	files = *(fd[_KEY_FILENAME] for fd in file_data),

	return Commit(sha, message, repo_identity, author, moment, files)


def get_repo_commits(repository, credentials, can_wait):
	"""
	Obtains data about all the commits in a GitHub repository through the
	GitHub API.

	Args:
		repository (str): a repository's full name in the format <owner>/<name>
		credentials (GitHubCredentials): the username and tokens of a GitHub
			user
		can_wait (bool): If it is set to True and and the GitHub API request
			rate limit is exceeded for all the user's tokens, the function
			waits for one hour until it can make more requests.

	Returns:
		list: all the commits (Commit) from the specified repository

	Raises:
		RuntimeError: if an error occured upon a request to the GitHub API
	"""
	commits = list()

	page_num = 1
	username = credentials.username
	token = credentials.get_next_token()

	# Loop through all the commit pages until the last returned empty page
	while True:
		try:
			all_commit_data = _request_commit_page(
				repository, page_num, username, token)

		except RuntimeError as rte:
			token = _catch_github_api_exception(rte, credentials, can_wait)
			continue

		commit_data_len = len(all_commit_data)
		if commit_data_len == 0:
			# Stop the loop if there are no more commits in the pages
			break

		# Iterate through the list of commits from the page
		commit_data_index = 0
		while commit_data_index < commit_data_len:
			commit_sha = all_commit_data[commit_data_index][_KEY_SHA]

			try:
				commit = _request_commit(commit_sha, repository, username, token)
				commits.append(commit)

			except RuntimeError as rte:
				token = _catch_github_api_exception(rte, credentials, can_wait)

				continue

			commit_data_index += 1

		page_num += 1

	return commits


def _raise_github_api_exception(api_data):
	if isinstance(api_data, dict):
		message = api_data.get(_KEY_MESSAGE)
		doc_url = api_data.get(_KEY_DOCUMENTATION_URL)

		if message is not None and doc_url is not None:
			raise RuntimeError(message + ". Documentation: " + doc_url)


def _repo_from_commit_api_url(url):
	path_commits_index = url.index(_PATH_COMMITS)
	repo_full_name =  url[_PATH_REPOS_LEN:path_commits_index]
	return RepoIdentity.from_full_name(repo_full_name)


def _request_commit(commit_sha, repository, username, token):
	"""
	Requests a commit from the GitHub API.

	Args:
		commit_sha (str): a SHA hash that identifies a commit
		repository (str): a GitHub repository name in the format <owner>/<name>
		username (str): a GitHub username
		token (str): a token owned by the specified GitHub user
	
	Returns:
		Commit: an object that contains the wanted commit's data

	Raises:
		RuntimeError: if the response indicates that an error occured
	"""
	commit_url = _PATH_REPOS + repository + _PATH_COMMITS + commit_sha
	commit_response = requests.get(commit_url, auth=(username, token))
	commit_data = json.loads(commit_response.content)

	_raise_github_api_exception(commit_data)

	commit = _commit_from_api_data(commit_data)
	return commit


def _request_commit_page(repository, page_num, username, token):
	"""
	Requests a page of commit data from the GitHub API.

	Args:
		repository (str): a GitHub repository name in the format <owner>/<name>
		page_num (int): the number of a commit page on the GitHub API, >= 1
		username (str): a GitHub username
		token (str): a token owned by the specified GitHub user

	Returns:
		list: the data of the commits from the wanted page

	Raises:
		RuntimeError: if the response indicates that an error occured
	"""
	commit_page_url = _PATH_REPOS + repository\
		+ '/commits?page=' + str(page_num)
	commits_response = requests.get(commit_page_url, auth=(username, token))
	commit_data = json.loads(commits_response.content)

	_raise_github_api_exception(commit_data)

	return commit_data
