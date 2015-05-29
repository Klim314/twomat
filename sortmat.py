#!/usr/bin/python3
import sys
from random import shuffle

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(arg1)

with open(arg1, 'r') as f:
	file1 = f.read().split('\n')
	file1 = [i.split("\t") for i in file1]
	if file1[-1] == ['']:
		file1.pop(-1)

with open(arg2, 'r') as f:
	file2 = f.read().split('\n')
	file2 = [i.split("\t") for i in file2]
	if file2[-1] == ['']:
		file2.pop(-1)
print(file2)
print()
file2 = list(zip(*file2))
file2 = [list(i) for i in file2]
file2[0][0] = '!'
print(file2)
shuffle(file2)
print(file2[0])
d = {i[0]:i for i in file2}
print(d)
