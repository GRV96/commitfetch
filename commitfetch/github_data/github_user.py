# __all__ declared at the module's end


class GitHubUser:
	"""
	This immutable class contains data about a GitHub user.

	Here, "login name" and "login" are used as synonyms of "username" for
	consistency with the GitHub API.
	"""

	# This class must stay immutable because instances are
	# stored in singleton GitHubUserRepository to be reused.

	def __init__(self, id, login, name):
		"""
		The constructor needs the user's ID, login name and real name.

		Parameters:
			id (int): this user's numeric ID.
			login (str): this user's login name.
			name (str): this user's real name.
		"""
		self._id = id
		self._login = login
		self._name = name

	def __repr__(self):
		return self.__class__.__name__\
			+ f"({repr(self._id)}, {repr(self._login)}, {repr(self._name)})"

	def __eq__(self, value):
		if not isinstance(value, GitHubUser):
			return False

		return\
			self._id == value._id\
			and self._login == value._login\
			and self._name == value._name

	@property
	def id(self):
		"""
		int: this user's numeric ID.
		"""
		return self._id
	
	@property
	def login(self):
		"""
		str: this user's login name.
		"""
		return self._login

	@property
	def name(self):
		"""
		str: this user's real name.
		"""
		return self._name


__all__ = [GitHubUser.__name__]
