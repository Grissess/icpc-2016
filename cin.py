import sys

inparts = sys.stdin.read().split()

def get():
	return inparts.pop(0)

def get_int():
	return int(get())
