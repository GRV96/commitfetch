class GitHubUserRepository:
	"""
	This singleton stores GitHubUser instances identified by their property
	login. Thus, it helps preventing the creation of many identical GitHubUser
	instances.
	"""

	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance._content = dict()

		return cls._instance

	def get_user(self, user_login):
		"""
		Obtains a GitHubUser instance identified by the user's login name,
		which corresponds to property GitHubUser.login.

		Parameters:
			user_login (str): the wanted user's login name.

		Returns:
			GitHubUser: data about the specified GitHub user, None if the user
				is not registered.
		"""
		github_user = self._content.get(user_login)
		return github_user

	def register_user(self, github_user):
		"""
		Registers a GitHubUser instance in this repository if the repository
		does not already contain it.

		Parameters:
			github_user (GitHubUser): data about a GitHub user.

		Returns:
			bool: True if the user was registered, False otherwise.
		"""
		was_user_registered = False
		user_login = github_user.login

		if user_login not in self._content:
			self._content[user_login] = github_user
			was_user_registered = True

		return was_user_registered


__all__ = [GitHubUserRepository.__name__]
