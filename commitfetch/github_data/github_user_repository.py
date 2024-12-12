"""
This module stores GitHubUser instances. It uses their property login as a key
to grant access to them. Thus, this module helps preventing the creation of
many identical GitHubUser instances.
"""


_repository_content = dict()


def get_github_user(user_login):
	"""
	Obtains data about a GitHub user specified by their login name, which
	corresponds to property GitHubUser.login.

	Parameters:
		user_login (str): the wanted user's login name.

	Returns:
		GitHubUser: data about the specified GitHub user, None if the user is
		not registered.
	"""
	github_user = _repository_content.get(user_login)
	return github_user


def register_github_user(github_user):
	"""
	Registers data about a GitHub user in the repository if this user is not
	registered.

	Parameters:
		github_user (GitHubUser): data about a GitHub user.

	Returns:
		bool: True if the user was registered, False otherwise.
	"""
	was_user_registered = False
	user_login = github_user.login

	if user_login not in _repository_content:
		_repository_content[user_login] = github_user
		was_user_registered = True

	return was_user_registered
