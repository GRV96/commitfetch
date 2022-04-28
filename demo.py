from argparse import\
	ArgumentParser
from pathlib import\
	Path

from commitfetch import\
	get_repo_commits,\
	GitHubCredentials


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"
_NEW_LINE = "\n"


def extract_text_lines(file_path, keep_blank_lines):
	"""
	Reads a text file and extracts its content as separate lines rather than a
	single string.

	Args:
		file_path (str or pathlib.Path): the path to a text file
		keep_blank_lines (bool): If False, the blank lines will be excluded
			from this function's output

	Returns:
		list: the lines of text extracted from the specified text file
	"""
	if isinstance(file_path, str):
		file_path = Path(file_path)

	with file_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as file:
		text = file.read()

	raw_lines = text.split(_NEW_LINE)

	if keep_blank_lines:
		return raw_lines

	lines = list()
	for line in raw_lines:
		if len(line) > 0:
			lines.append(line)

	return lines


def make_arg_parser():
	parser = ArgumentParser()
	parser.add_argument("-r", "--repository", type=str, required=True,
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

#repository = "scottyab/rootbeer" # 191 commits
#repository = "mendhak/gpslogger" # 2233 commits
repository = args.repository
token_file = args.token_file
username = args.username
can_wait = args.can_wait

tokens = extract_text_lines(token_file, False)
credentials = GitHubCredentials(username, tokens)
commits = get_repo_commits(repository, credentials, can_wait)

first_commit = commits[0]

print("First commit")
print(f"SHA: {first_commit.sha}")
print(f"Repository: {first_commit.repository}")
print(f"Author: {first_commit.author}")
print(f"Moment: {first_commit.moment_to_str()}")
print("Files:")
for file in first_commit.files:
	print(f"\t{file}")
