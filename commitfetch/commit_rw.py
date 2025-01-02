# __all__ declared at the module's end

from sys import\
	modules as sys_modules

from repr_rw import\
	read_reprs,\
	write_reprs


_LIB_NAME = "commitfetch"

_COMMIT_READING_IMPORTATIONS = ("from commitfetch import GitHubUser, Commit",)


def _add_lib_to_sys_modules():
	from pathlib import Path
	# syspathmodif is a dependency of repr_rw.
	from syspathmodif import sp_append

	# Storing a string avoids the conversion by syspathmodif.
	repo_root = str(Path(__file__).resolve().parents[1])
	was_repo_root_appended = sp_append(repo_root)

	# The import includes commitfetch in sys.modules.
	import commitfetch

	if was_repo_root_appended:
		# Leave repo_root if it was initially in sys.path.
		from syspathmodif import sp_remove
		sp_remove(repo_root)


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

	if _LIB_NAME not in sys_modules:
		_add_lib_to_sys_modules()

	commit_generator = read_reprs(file_path, _COMMIT_READING_IMPORTATIONS)
	yield from commit_generator


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


__all__ = [
	read_commit_reprs.__name__,
	write_commit_reprs.__name__
]
