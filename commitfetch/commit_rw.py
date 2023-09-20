from pathlib import\
	Path

from repr_rw import\
	read_reprs,\
	write_reprs


_COMMIT_READING_IMPORTATION =\
	{"from commit import Commit": Path(".").resolve()}


def read_commit_reprs(file_path):
	return read_reprs(file_path, _COMMIT_READING_IMPORTATION)


def write_commit_reprs(file_path, commits):
	"""
	Writes the representation of Commit instances in a text file. Each line is
	a string returned by function repr. If the file already exists, this
	function will overwrite it.

	Args:
		file_path (str or pathlib.Path): the path to the text file that will
			contains the Commit representations
		objs (list, set or tuple): the Commit instances whose representation
			will be written
	"""
	write_reprs(file_path, commits)
