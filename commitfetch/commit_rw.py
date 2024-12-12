from pathlib import\
	Path

from repr_rw import\
	read_reprs,\
	write_reprs


_REPO_DIR = Path(__file__).resolve().parents[1]
_COMMIT_READING_IMPORTATIONS = {
	"from commitfetch import GitHubUser": _REPO_DIR,
	"from commitfetch import Commit": _REPO_DIR}


def read_commit_reprs(file_path):
	"""
	This generator reads a text file that contains the representations of
	Commit instances and recreates those objects. Each iteration yields a
	Commit instance. The representations are strings returned by function
	repr. Each line in the file must be a Commit representation. Empty lines
	are ignored.

	Parameters:
		file_path (str or pathlib.Path): the path to a text file that contains
			Commit representations.

	Yields:
		Commit: a Commit instance recreated from its representation.

	Raises:
		FileNotFoundError: if argument file_path does not exist.
		TypeError: if argument file_path is not of type str or pathlib.Path.
		Exception: any exception raised upon the parsing of a Commit
			representation.
	"""
	commit_generator = read_reprs(file_path, _COMMIT_READING_IMPORTATIONS)
	return commit_generator


def write_commit_reprs(file_path, commits):
	"""
	Writes the representations of Commit instances in a text file. The
	representations are strings returned by function repr. Each line of the
	file is a representation. If the file already exists, this function will
	overwrite it.

	Parameters:
		file_path (str or pathlib.Path): the path to the text file that will
			contain the Commit representations.
		commits (generator, list, set or tuple): the Commit instances whose
			representation will be written.
	"""
	write_reprs(file_path, commits)
