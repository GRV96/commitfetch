from argparse import\
	ArgumentParser
from pathlib import\
	Path

from commitfetch import\
	read_reprs


def make_arg_parser():
	parser = ArgumentParser()
	parser.add_argument("-c", "--commit-file", type=Path, required=True,
		help="Each line of this file contains a representation"
			+ "of an instance of Commit.")

	return parser


parser = make_arg_parser()
args = parser.parse_args()
commit_path = args.commit_file

commits = read_reprs(commit_path)

first_commit = commits[0]

print("First commit")
print(f"SHA: {first_commit.sha}")
print(f"Message: {first_commit.message}")
print(f"Repository: {first_commit.repository}")
print(f"Author: {first_commit.author}")
print(f"Moment: {first_commit.moment_to_str()}")
print("Files:")
for file in first_commit.files:
	print(f"\t{file}")