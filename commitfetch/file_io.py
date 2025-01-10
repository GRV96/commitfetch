# __all__ declared at the module's end

# strath is an indirect dependency of repr_rw.
from strath import\
	ensure_path_is_pathlib


_COLON = ":"

_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def read_github_credentials(file_path):
	"""
	This generator provides GitHub credentials stored in a text file. Each line
	must consist of a GitHub username and a personal access token (PAT) owned
	by the corresponding user separated by a colon. Whitespaces are allowed
	before and after the colon. Empty lines are ignored. Each iteration yields
	one credential made of a username and a PAT.

	Examples of valid lines in the credential file:

	MyUsername:ghp_a1b2c3d4e5f6

	MyUsername: ghp_a1b2c3d4e5f6

	MyUsername : ghp_a1b2c3d4e5f6

	Parameters:
		file_path (str or pathlib.Path): the path to a text file containing
			GitHub credentials.

	Yields:
		tuple: a GitHub credential consisting of a username (str, index 0) and
			a PAT (str, index 1).

	Raises:
		FileNotFoundError: if argument file_path does not exist.
		TypeError: if argument file_path is not of type str or pathlib.Path.
		ValueError: if a line in the text file does not match the required
			format.
	"""
	file_path = ensure_path_is_pathlib(file_path, False)

	with file_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as file:
		for line in file:
			# The iterator yields one line at the time, including '\n'.
			line = line.strip()

			if len(line) == 0:
				# Ignore empty lines.
				continue

			credential = line.split(_COLON)

			if len(credential) != 2:
				raise ValueError(f"Invalid GitHub credential: {credential}")

			# Whitespaces may precede or follow the colon.
			username = credential[0].strip()
			token = credential[1].strip()

			yield (username, token)


__all__ = [read_github_credentials.__name__]
