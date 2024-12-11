"""
This module stores GitHubUser instances for later use.
It can prevent the creation of many identical instances.
"""


_repository_content = dict()


def get_github_user(user_login):
	"""
	Obtains data about a GitHub user specified by their login name.

	Parameters:
		user_login (str): the wanted user's login name.

	Returns:
		GitHubUser: data about the specified GitHub user or None if the user
			is not registered.
	"""
	github_user = _repository_content.get(user_login)
	return github_user


def register_github_user(github_user):
	"""
	Registers data about a GitHub user in the repository if the user is not
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
