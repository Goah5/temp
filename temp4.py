import win32clipboard
from time import sleep


def replace(s: str):
	# set clipboard data
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(s)
	win32clipboard.CloseClipboard()


def read() -> str:
	# get clipboard data
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data


def f(s: str) -> str:
	if "workshop_download_item 294100 " in s:
		return s
	else:
		return "workshop_download_item 294100 "+s[s.index("?id=")+4:len(s)]


def main():
	while 1:
		sleep(1)
		try:
			replace(f(read()))
		except:
			print('An exception occurred')
			


if __name__ == "__main__":
	main()
