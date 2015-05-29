#!/usr/bin/python3
#given a list of negative correlations returns the SP and count values for each

import sys
speciesFile = sys.argv[1]
koFile = sys.argv[2]
targetFile = sys.argv[3]

with open(targetFile, 'r') as f:
	base = f.read()
	base = base.split("\n")
	base = [i.split('\t') for i in base]
	if base[-1] == ['']:
		base.pop(-1)

with open(speciesFile, 'r') as f:
	species = f.read().split('\n')
	species = [i.split("\t") for i in species]
	if species[-1] == ['']:
		species.pop(-1)

with open(koFile, 'r') as f:
	ko = f.read().split('\n')
	ko = [i.split("\t") for i in ko]
	if ko[-1] == ['']:
		ko.pop(-1)

#terms to be extracted
grab = []
for i in base:
	grab.append((i[0], i[1]))

#includes the first useless entry
sampleCount = len(species[0])
result = [[i for i in species[0]]]
sampleDict = {species[0][i]: i for i in range(sampleCount)}
spDict = {species[i][0]: i for i in range(len(species))}
koDict = {ko[i][0]: i for i in range(len(ko))}



for i in grab:
	result.append([i[0]+'#'+ i[1]] + [species[spDict[i[0]]][j]+ '#' + ko[koDict[i[0]]] [j] for j in range(1, sampleCount) ])
print(result)
print()
result = ["\t".join(i) for i in result]
with open('negExtract.out','w') as f:
	print(result)
	f.write("\n".join(result))






