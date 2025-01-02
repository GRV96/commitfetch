from . import _recurring_strings as rs


class GitHubUser:
	"""
	This immutable class contains data about a GitHub user.
	"""

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
		return self.__class__.__name__ + rs.PAR_OPENING\
			+ str(self._id) + rs.COMMA_SPACE\
			+ rs.QUOTE + self._login + rs.QUOTE + rs.COMMA_SPACE\
			+ rs.QUOTE + self._name + rs.QUOTE + rs.PAR_CLOSING

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
