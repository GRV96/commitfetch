# __all__ declared at the module's end


class GitHubCredRepository:
	"""
	A GitHub credential consists of a GitHub username and a personal access
	token (PAT) owned by the specified user. This class stores tuples
	containing a username (str, index 0) and a token (str, index 1). These
	credentials in the form of tuples can be directly used to authenticate a
	request to the GitHub API.

	The GitHub API allows 5000 authenticated requests per user per hour. To
	facilitate sending many requests in a short period, this class allows to
	iterate through the credentials.
	"""

	def __init__(self, credentials):
		"""
		The constructor requires GitHub credentials.

		Parameters:
			credentials (generator, list, set or tuple): GitHub credentials.

		Raises:
			ValueError: if argument credentials contains less than one element.
		"""
		self._credentials = tuple(credentials)
		if len(self._credentials) < 1:
			raise ValueError("At least one credential must be provided.")

		self.reset_credential_iter()

	def get_next_credential(self):
		"""
		The next unused credential becomes the current credential unless all
		credentials have been used.

		Returns:
			tuple: the next unused credential, None if all credentials have been used.
		"""
		try:
			credential = next(self._cred_iterator)
		except StopIteration:
			credential = None

		return credential

	def reset_credential_iter(self):
		"""
		Resets the itertion through the credentials performed by method
		get_next_credential.
		"""
		self._cred_iterator = iter(self._credentials)

	@property
	def credentials(self):
		"""
		tuple: the GitHub credentials stored in this instance.
		"""
		return self._credentials


__all__ = [GitHubCredRepository.__name__]
