"""
This demo shows how this library allows to obtain commit data through the
GitHub API and store the written representation of Commit objects in a text
file. The representations are strings returned by a call of function repr on a
Commit instance.
"""


from argparse import\
	ArgumentParser
from datetime import\
	datetime
from pathlib import\
	Path

# syspathmodif is a dependency of repr_rw.
from syspathmodif import\
	sp_append,\
	sp_remove

_REPO_ROOT = Path(__file__).resolve().parents[1]
sp_append(_REPO_ROOT)
from commitfetch import\
	RepoIdentity,\
	get_repo_commits,\
	read_github_credentials,\
	write_commit_reprs
sp_remove(_REPO_ROOT)


def make_arg_parser():
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-r", "--repository",
		type=RepoIdentity.from_full_name,
		required=True,
		help="A GitHub repository name in the form <owner>/<name>")
	parser.add_argument("-c", "--cred-file", type=Path, required=True,
		help="This file must list GitHub credentials one per line.")
	parser.add_argument("-w", "--can-wait", action="store_true",
		help="Wait one hour if request rate exceeded and no token left.")

	return parser


parser = make_arg_parser()
args = parser.parse_args()
repository = args.repository
cred_file = args.cred_file.resolve()
can_wait = args.can_wait

cred_generator = read_github_credentials(cred_file)
commit_generator = get_repo_commits(str(repository), cred_generator, can_wait)

dt_now = datetime.now
commit_file_path = repository.get_full_name("_") + "_commits.txt"
try:
	start_moment = dt_now()
	write_commit_reprs(commit_file_path, commit_generator)
finally:
	end_moment = dt_now()
	exec_time = end_moment - start_moment
	print(f"Execution time: {exec_time} ({exec_time.total_seconds()} seconds)")
