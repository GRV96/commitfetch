class GitHubCredentials:
	"""
	The credentials consist of a username and tokens owned by the user in
	question. Methods get_next_token and reset_token_iter facilitate the
	iteration through the tokens.
	"""

	def __init__(self, username, tokens):
		"""
		The constructor requires a username and a container of tokens.

		Args:
			username (str): a GitHub username
			tokens: a container of GitHub tokens (str)

		Raises:
			ValueError: if tokens contains less than one element
		"""
		if len(tokens) < 1:
			raise ValueError("At least one token must be provided.")

		self._username = username
		self._tokens = tuple(tokens)
		self.reset_token_iter()

	def get_next_token(self):
		"""
		Each token allows 2000 authenticated requests to the GitHub API per
		hour. For the purpose of making many requests in a short period, this
		method allows to obtain the next unused token stored here.

		Returns:
			str: the next unused token
			None: if all tokens have been used
		"""
		try:
			token = next(self._token_iter)
		except StopIteration:
			token = None

		return token

	def reset_token_iter(self):
		"""
		Resets the token itertion performed by method get_next_token.
		"""
		self._token_iter = iter(self._tokens)

	@property
	def tokens(self):
		"""
		tuple: tokens (str) owned by this GitHub user
		"""
		return self._tokens

	@property
	def username(self):
		"""
		str: this GitHub user's name
		"""
		return self._username
