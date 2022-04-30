from argparse import\
	ArgumentParser
from pathlib import\
	Path

from commitfetch import\
	get_repo_commits,\
	extract_text_lines,\
	GitHubCredentials,\
	RepoIdentity,\
	write_reprs


def make_arg_parser():
	parser = ArgumentParser()
	parser.add_argument("-r", "--repository",
		type=RepoIdentity.from_full_name,
		required=True,
		help="A GitHub repository name in the form <owner>/<name>")
	parser.add_argument("-t", "--token-file", type=Path, required=True,
		help="This file must list GitHub tokens owned by -u one by line.")
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

tokens = extract_text_lines(token_file, False)
credentials = GitHubCredentials(username, tokens)
commits = get_repo_commits(str(repository), credentials, can_wait)

write_reprs(repository.get_full_name("_") + "_commits.txt", commits)
