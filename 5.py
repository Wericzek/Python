import os

path = "/Users/plweopy/Desktop/python"
print(os.listdir(path))

for file in os.listdir(path):
	print(file)