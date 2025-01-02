__all__ = ["RepoIdentity"]

from . import recurring_strings as rs


_SLASH = "/"


class RepoIdentity:
	"""
	This class comprises the name of a GitHub repository's owner and the
	repository's name, which constitute the repository's identity.
	"""

	def __init__(self, owner, name):
		"""
		The constructor requires the repository's owner and name.

		Parameters:
			owner (str): the name of the repository's owner.
			name (str): the repository's name.
		"""
		self._owner = owner
		self._name = name

	def __repr__(self):
		return self.__class__.__name__ + rs.PAR_OPENING\
			+ rs.QUOTE + self._owner + rs.QUOTE_COMMA_SPACE\
			+ rs.QUOTE + self._name + rs.QUOTE_PAR_CLOSING\

	def __str__(self):
		return self.get_full_name()

	@staticmethod
	def from_full_name(full_name):
		"""
		Makes a RepoIdentity from a repository's full name, in the format
		<owner>/<name>.

		Parameters:
			full_name (str): a repository's full name in the prescibed format.

		Returns:
			RepoIdentity: an object that identifies the indicated repository.

		Raises:
			ValueError: if parameter full_name is not in the expected format.
		"""
		split_name = full_name.split(_SLASH)

		if len(split_name) != 2:
			raise ValueError(
				"The repository name must be in the format <owner>/<name>.")

		return RepoIdentity(split_name[0], split_name[1])

	def get_full_name(self, separator=_SLASH):
		"""
		Provides the repository's full name by joining the owner's name and the
		repository's name with the given separator. Calling this method without
		specifying a separator is equivalent to using function str.

		Parameters:
			separator (str): It comes between the owner's name and the
				repository's name. Defaults to '/'.

		Returns:
			str: the repository's full name in the format
				<owner><separator><name>.
		"""
		return self._owner + separator + self._name

	@property
	def name(self):
		"""
		str: the repository's name.
		"""
		return self._name

	@property
	def owner(self):
		"""
		str: the name of the repository's owner.
		"""
		return self._owner
