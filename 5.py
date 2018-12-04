import os

import sys

def FileTree(path, level):
	for roots, dirs, files in os.walk(path):
		deep = level * "    "

		for dir in dirs:
			sys.stdout.write(deep + "- " + dir + "\n\r")
			path2 = path + "/" + dir
			level2 = level + 1
			FileTree(path2, level2)

		for file in files:
			sys.stdout.write(deep + ">" + file + "\n\r")

		break;

	return;


mPath = "/Users/plweopy/Desktop/python"
print("File tree: ", mPath, "\n\r")
FileTree(mPath, 0)