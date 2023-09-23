from pathlib import\
	Path


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"
_NEW_LINE = "\n"


def extract_text_lines(file_path, keep_blank_lines):
	"""
	Reads a text file and extracts its content as separate lines rather than a
	single string.

	Args:
		file_path (str or pathlib.Path): the path to a text file
		keep_blank_lines (bool): If it is False, the blank lines will be
			excluded from this function's output.

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

	lines = [line for line in raw_lines if len(line) > 0]

	return lines
