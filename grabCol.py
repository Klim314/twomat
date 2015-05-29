#!/usr/bin/env python3
import sys

target = sys.argv[1]
out = sys.argv[2]

holder = []
with open(target) as f:
	holder.extend(f.readline().strip().split('\t')[1:])
	for i in f:
		holder.append(i.strip().split('\t')[0])

print(holder)

with open(out, 'w') as f:
	f.write('\t'.join(holder))
