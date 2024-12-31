import sys

from pathlib import\
	Path

from repr_rw import\
	read_reprs,\
	write_reprs
from syspathmodif import\
	sp_append,\
	sp_remove


_LIB_NAME = "commitfetch"

# Storing a string rather than a Path avoids the conversion by syspathmodif.
_REPO_ROOT = str(Path(__file__).resolve().parents[1])

_COMMIT_READING_IMPORTATIONS = ("from commitfetch import GitHubUser, Commit",)


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
	# When this generator is being used, package commitfetch has presumably
	# been imported at least once and thus, included in sys.modules. This makes
	# commitfetch available for import with no modifications to sys.path.

	# The next block ensures the presence of commitfetch in sys.modules.
	if _LIB_NAME not in sys.modules:
		sp_append(_REPO_ROOT)
		import commitfetch # Now, commitfetch is in sys.modules.
		sp_remove(_REPO_ROOT)

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
