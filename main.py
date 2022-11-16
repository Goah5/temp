import os


def create_file(file_name=".temp", file_number="", file_extension=".py"):
	with open(file_name+file_number+file_extension, "w") as somefile:
		pass  # так надо


def sifting(list):
	temp = []
	for i in list:
		if ".temp" in i:
			temp.append(i)
	return temp


def x(list):
	temp = []
	for i in list:
		temp.append(int(i[5:-3]))
	return temp


if __name__ == "__main__":
	create_file(".temp", str(max(x(sifting(os.listdir())))+1))
