from pathlib import\
	Path

from .commit import\
	Commit


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"
_MODE_W = "w"
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

	lines = [line for line in raw_lines if len(line) > 0]

	return lines


def read_reprs(file_path):
	"""
	If a text file contains the representation of Python objects, this function
	can read it to recreate those objects. Each line must contain the string
	returned by a call to function repr.

	This function works only for instances of Commit and objects whose type
	does not need to be imported.

	Args:
		file_path (str or pathlib.Path): the path to a text file that contains
			object representations

	Returns:
		list: the objects recreated from their representation
	"""
	objs_reprs = extract_text_lines(file_path, False)
	objs = list()

	for obj_repr in objs_reprs:
		objs.append(eval(obj_repr))

	return objs


def write_reprs(file_path, objs):
	"""
	Writes the representation of Python objects in a text file. Each line
	contains the string returned by a call to function repr. If the file
	already exists, this function will overwrite it.

	Args:
		file_path (str or pathlib.Path): the path to the text file that will
			contains the object representations
		objs (container): the objects whose representation will be written
	"""
	if isinstance(file_path, str):
		file_path = Path(file_path)

	with file_path.open(mode=_MODE_W, encoding=_ENCODING_UTF8) as file:

		for obj in objs:
			file.write(repr(obj) + _NEW_LINE)
