# __all__ declared at the module's end

from datetime import datetime
from pathlib import Path

from .repo_identity import RepoIdentity


_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def _datetime_from_str(datetime_str):
	return datetime.strptime(datetime_str, _DATETIME_FORMAT)

def _datetime_to_str(datetime_obj):
	return datetime.strftime(datetime_obj, _DATETIME_FORMAT)


class Commit:
	"""
	A commit in a GitHub repository.
	"""

	def __init__(self, sha, message, repository, moment, author, files):
		"""
		The GitHub commit constructor.

		Parameters:
			sha (str): the SHA hash that identifies this commit.
			message (str): the description of the modifications recorded in
				this commit.
			repository (str or RepoIdentity): the repository that contains this
				commit. If this argument is a string, it will be processed by
				RepoIdentity.from_full_name.
			moment (str or datetime.datetime): the moment when this commit was
				made. If it is a string, it must match format
				%Y-%m-%dT%H:%M:%SZ.
			author (GitHubUser): the GitHub user who made this commit.
			files (generator, list, set or tuple): the paths
				(str or pathlib.Path) to the files created, modified or deleted
				in this commit.

		Raises:
			ValueError: if argument repository or moment is a string and does
				not match the expected format.
		"""
		self._sha = sha
		self._message = message
		self._author = author

		self._repository =\
			RepoIdentity.from_full_name(repository)\
			if isinstance(repository, str)\
			else repository

		self._moment =\
			_datetime_from_str(moment)\
			if isinstance(moment, str)\
			else moment

		self._files = *(Path(file) for file in files),

	def __repr__(self):
		paths_as_strings = *(str(file) for file in self._files),

		arguments = (
			self._sha,
			self._message,
			str(self._repository),
			self.moment_to_str(),
			self._author,
			paths_as_strings
		)

		return self.__class__.__name__ + repr(arguments)

	@property
	def author(self):
		"""
		GitHubUser: the GitHub user who made this commit.
		"""
		return self._author

	@property
	def files(self):
		"""
		tuple: the paths (pathlib.Path) to the files created, modified or
			deleted in this commit.
		"""
		return self._files

	@property
	def message(self):
		"""
		str: the description of the modifications recorded in this commit.
		"""
		return self._message

	@property
	def moment(self):
		"""
		datetime.datetime: the moment when this commit was made.
		"""
		return self._moment

	def moment_to_str(self):
		"""
		Converts the moment of this commit to a string in the format
		%Y-%m-%dT%H:%M:%SZ.

		Returns:
			str: the moment when this commit was made.
		"""
		return _datetime_to_str(self._moment)

	@property
	def repository(self):
		"""
		RepoIdentity: the repository that contains this commit.
		"""
		return self._repository

	@property
	def sha(self):
		"""
		str: the SHA hash that identifies this commit.
		"""
		return self._sha


__all__ = [Commit.__name__]
