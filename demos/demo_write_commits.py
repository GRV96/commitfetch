"""
This demo shows how this library allows to obtain commit data through the
GitHub API and store the written representation of Commit objects in a text
file. The representations are strings returned by a call of function repr on a
Commit instance.
"""


from argparse import\
	ArgumentParser
from pathlib import\
	Path

from syspathmodif import\
	sp_append,\
	sp_remove

_REPO_ROOT = Path(__file__).resolve().parents[1]
sp_append(_REPO_ROOT)
from commitfetch import\
	GitHubCredentials,\
	RepoIdentity,\
	extract_text_lines,\
	get_repo_commits,\
	write_commit_reprs
sp_remove(_REPO_ROOT)


def make_arg_parser():
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-r", "--repository",
		type=RepoIdentity.from_full_name,
		required=True,
		help="A GitHub repository name in the form <owner>/<name>")
	parser.add_argument("-t", "--token-file", type=Path, required=True,
		help="This file must list GitHub tokens owned by -u one per line.")
	parser.add_argument("-u", "--username", type=str, required=True,
		help="A GitHub username")
	parser.add_argument("-w", "--can-wait", action="store_true",
		help="Wait one hour if request rate exceeded and no token left.")

	return parser


parser = make_arg_parser()
args = parser.parse_args()
repository = args.repository
token_file = args.token_file
username = args.username
can_wait = args.can_wait

token_generator = extract_text_lines(token_file, False)
credentials = GitHubCredentials(username, token_generator)
commit_generator = get_repo_commits(str(repository), credentials, can_wait)

write_commit_reprs(repository.get_full_name("_") + "_commits.txt", commit_generator)
