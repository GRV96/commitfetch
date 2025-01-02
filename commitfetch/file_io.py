# strath is an indirect dependency of repr_rw.
from strath import\
	ensure_path_is_pathlib


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def extract_text_lines(file_path, keep_blank_lines):
	"""
	This generator reads a text file and extracts its content as separate lines
	rather than a single string. Each iteration yields one line.

	Parameters:
		file_path (str or pathlib.Path): the path to a text file.
		keep_blank_lines (bool): The blank lines are yeilded if and only if
			this argument is True.

	Yields:
		str: a line of text extracted from the specified text file.

	Raises:
		FileNotFoundError: if argument file_path does not exist.
		TypeError: if argument file_path is not of type str or pathlib.Path.
	"""
	file_path = ensure_path_is_pathlib(file_path, False)

	with file_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as file:
		for line in file:
			line = line[:-1] # Remove '\n' from the line's end.

			if keep_blank_lines or len(line) > 0:
				yield line


__all__ = [extract_text_lines.__name__]
