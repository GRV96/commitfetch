import json
import requests

from .github_user import GitHubUser


_KEY_ID = "id"
_KEY_LOGIN = "login"
_KEY_NAME = "name"

_PATH_USERS = "https://api.github.com/users/"


def _github_user_from_api_data(github_user_data):
	id = github_user_data[_KEY_ID]
	login = github_user_data[_KEY_LOGIN]
	name = github_user_data[_KEY_NAME]
	return GitHubUser(id, login, name)


class GitHubUserRequester:
	"""
	This class makes requests for GitHub user data to the GitHub API.
	Obtained data is cached to avoid repetitive requests.
	"""

	def __init__(self):
		"""
		The constructor initializes the user data cache.
		"""
		self._github_user_cache = dict()

	def get_github_user(self, user_login, username, token):
		github_user = self._github_user_cache.get(username)

		if github_user is None:
			user_url = _PATH_USERS + user_login
			user_response = requests.get(user_url, auth=(username, token))
			user_data = json.loads(user_response.content)

			github_user = _github_user_from_api_data(user_data)
			self._github_user_cache[username] = github_user

		return github_user
