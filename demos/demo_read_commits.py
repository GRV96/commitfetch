"""
This demo shows how this library allows to read commit representations from a
text file and convert them to Commit instances. The representations are strings
returned by a call of function repr on a Commit instance.
"""


from argparse import\
	ArgumentParser
from pathlib import\
	Path

# syspathmodif is a dependency of repr_rw.
from syspathmodif import\
	sp_append,\
	sp_remove

_REPO_ROOT = Path(__file__).resolve().parents[1]
sp_append(_REPO_ROOT)
from commitfetch import\
	read_commit_reprs
sp_remove(_REPO_ROOT)


def make_arg_parser():
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-c", "--commit-file", type=Path, required=True,
		help="Each line of this text file contains a representation"
			+ " of a Commit instance.")

	return parser


parser = make_arg_parser()
args = parser.parse_args()
commit_file = args.commit_file

commit_generator = read_commit_reprs(commit_file)

first_commit = next(commit_generator)

print("First commit")
print(f"SHA: {first_commit.sha}")
print(f"Message: {first_commit.message}")
repository = first_commit.repository
print(f"Repository: {repository} - {repr(repository)}")
print(f"Moment: {first_commit.moment_to_str()}")
print(f"Author: {first_commit.author}")
print("Files:")
for file in first_commit.files:
	print(f"\t{file}")
