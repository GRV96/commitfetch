class GitHubCredentials:
	"""
	The credentials consist of a username and personal authentication tokens
	(PATs) owned by the user in question. The username and a token can
	constitute an authentication for a request to the GitHub API.

	The GitHub API allows 5000 authenticated requests per hour. To facilitate
	sending many requests in a short period, this class allows to iterate
	through the tokens.
	"""

	def __init__(self, username, tokens):
		"""
		The constructor requires a username and a container of tokens.

		Parameters:
			username (str): a GitHub username.
			tokens (generator, list, set or tuple): GitHub tokens (str) owned
				by the specified user.

		Raises:
			ValueError: if argument tokens contains less than one element.
		"""
		self._username = username
		self._tokens = tuple(tokens)
		if len(self._tokens) < 1:
			raise ValueError("At least one token must be provided.")

		self.reset_token_iter()

	def get_next_token(self):
		"""
		The next unused token becomes the current token unless all tokens have
		been used.

		Returns:
			str: the next unused token, None if all tokens have been used.
		"""
		try:
			token = next(self._token_iter)
		except StopIteration:
			token = None

		return token

	def reset_token_iter(self):
		"""
		Resets the itertion through the tokens performed by method
		get_next_token.
		"""
		self._token_iter = iter(self._tokens)

	@property
	def tokens(self):
		"""
		tuple: tokens (str) owned by this GitHub user.
		"""
		return self._tokens

	@property
	def username(self):
		"""
		str: this GitHub user's name.
		"""
		return self._username


__all__ = [GitHubCredentials.__name__]
