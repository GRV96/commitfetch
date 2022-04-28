from datetime import datetime
from pathlib import Path


_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

_CLOSING_PAR = ")"
_COMMA_SPACE = ", "
_OPENING_PAR = "("
_QUOTE = "'"
_QUOTE_CLOSING_PAR = _QUOTE + _CLOSING_PAR
_QUOTE_COMMA_SPACE = _QUOTE + _COMMA_SPACE
_SLASH = "/"


class Commit:
	"""
	A commit in a GitHub repository
	"""

	def __init__(self, sha, repository, author, moment, files):
		"""
		The GitHub commit constructor

		Args:
			sha (str): the SHA hash that identifies this commit
			repository (RepoIdentity): the repository that contains this commit
			author (str): the login name of the commit's author
			moment (str or datetime. datetime): the moment when this commit
				was made. If it is a string, it must match format
				"%Y-%m-%dT%H:%M:%SZ".
			files (container): the paths to the files created, modified or
				deleted in this commit as strings or pathlib.Path objects
		"""
		self._sha = sha
		self._repository = repository
		self._author = author

		self._moment = moment
		if isinstance(self._moment, str):
			self._moment = _datetime_from_str(self._moment)

		self._files = *(Path(file) for file in files),

	def __repr__(self):
		str_paths = *(str(file) for file in self._files),

		return self.__class__.__name__ + _OPENING_PAR\
			+ _QUOTE + self._sha + _QUOTE_COMMA_SPACE\
			+ _QUOTE + repr(self._repository) + _QUOTE_COMMA_SPACE\
			+ _QUOTE + self._author + _QUOTE_COMMA_SPACE\
			+ _QUOTE + _datetime_to_str(self._moment) + _QUOTE_COMMA_SPACE\
			+ str(str_paths) + _CLOSING_PAR

	@property
	def author(self):
		"""
		str: the login name of the commit's author
		"""
		return self._author

	@property
	def files(self):
		"""
		tuple: the paths to the files created, modified or deleted in this
		commit as pathlib.Path objects
		"""
		return self._files

	@property
	def moment(self):
		"""
		datetime.datetime: the moment when this commit was made
		"""
		return self._moment

	def moment_to_str(self):
		"""
		Converts the moment of this commit to a string in the format
		%Y-%m-%dT%H:%M:%SZ.

		Returns:
			str: the moment when this commit was made
		"""
		return _datetime_to_str(self._moment)

	@property
	def repository(self):
		"""
		RepoIdentity: the repository that contains this commit
		"""
		return self._repository

	@property
	def sha(self):
		"""
		str: the SHA hash that identifies this commit
		"""
		return self._sha


class RepoIdentity:
	"""
	The identity of a GitHub repository
	"""

	def __init__(self, owner, name):
		"""
		The constructor requires the repository's owner and name.

		Args:
			owner (str): the name of the repository's owner
			name (str): the repository's name
		"""
		self._owner = owner
		self._name = name

	def __repr__(self):
		return self.__class__.__name__ + _OPENING_PAR\
			+ _QUOTE + self._owner + _QUOTE_COMMA_SPACE\
			+ _QUOTE + self._name + _QUOTE_CLOSING_PAR\

	def __str__(self):
		return self._owner + _SLASH + self._name

	@staticmethod
	def from_full_name(full_name):
		"""
		Makes a RepoIdentity from a repository's full name, in the format
		<owner>/<name>.

		Args:
			full_name (str): a repository's full name in the prescibed format

		Returns:
			RepoIdentity: an object that identifies the indicated repository

		Raises:
			ValueError: if parameter full_name is not in the right format
		"""
		split_name = full_name.split(_SLASH)

		if len(split_name) != 2:
			raise ValueError(
				"The repository name must be in the format <owner>/<name>.")

		return RepoIdentity(split_name[0], split_name[1])

	@property
	def name(self):
		"""
		str: the repository's name
		"""
		return self._name

	@property
	def owner(self):
		"""
		str: the name of the repository's owner
		"""
		return self._owner


def _datetime_from_str(datetime_str):
	return datetime.strptime(datetime_str, _DATETIME_FORMAT)


def _datetime_to_str(datetime_obj):
	return datetime.strftime(datetime_obj, _DATETIME_FORMAT)
