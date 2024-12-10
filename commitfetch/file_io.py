from pathlib import\
	Path


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def _ensure_is_path(obj):
	if isinstance(obj, Path):
		return obj

	elif isinstance(obj, str):
		return Path(obj)

	else:
		raise TypeError(
			"An argument of type str or pathlib.Path is expected.")


def extract_text_lines(file_path, keep_blank_lines):
	"""
	This generator reads a text file and extracts its content as separate lines
	rather than a single string. Each iteration yields one line.

	Parameters:
		file_path (str or pathlib.Path): the path to a text file.
		keep_blank_lines (bool): If it is False, the blank lines will be
			excluded from this function's output.

	Yields:
		str: a line of text extracted from the specified text file.

	Raises:
		FileNotFoundError: if argument file_path does not exist.
		TypeError: if argument file_path is not of type str or pathlib.Path.
	"""
	file_path = _ensure_is_path(file_path)

	if keep_blank_lines:
		is_line_accepted = lambda line: True
	else:
		is_line_accepted = lambda line: len(line) > 0

	with file_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as file:
		for line in file:
			if is_line_accepted(line):
				yield line
