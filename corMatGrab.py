#!/usr/bin/python3

#Takes two correlation matrices drawn from twoMAT and extracts values which meet thresholds
#format: ./twoMat.py <corMat> <pMat> <coreCut> <pCut>

import sys


#system arguments
arg1 = sys.argv[1] 		#corMat
arg2 = sys.argv[2]	 	#pMat
coreCut = float(sys.argv[3])	#coreCut
pCut = float(sys.argv[4]) 		#pCut
with open(arg1, 'r') as f:
	corMat = f.read().split('\n')
	corMat = [i.split("\t") for i in corMat]
	if corMat[-1] == ['']:
		corMat.pop(-1)

with open(arg2, 'r') as f:
	pMat = f.read().split('\n')
	pMat = [i.split("\t") for i in pMat]
	if pMat[-1] == ['']:
		pMat.pop(-1)


resLst, posResLst, negResLst = [],[],[]

#for all numerical values
for i in range(1,len(corMat)):
	for j in range(1, len(corMat[0])):
		if abs(float(corMat[i][j])) > coreCut and float(pMat[i][j]) < pCut:
			#Species, KO, cor, p
			resLst.append((corMat[0][j], pMat[i][0], corMat[i][j], pMat[i][j], '-' if float(corMat[i][j]) < 0 else '+' ))
		if float(corMat[i][j]) > coreCut and float(pMat[i][j]) < pCut:
			#Species, KO, cor, p
			posResLst.append((corMat[0][j], pMat[i][0], corMat[i][j], pMat[i][j], '-' if float(corMat[i][j]) < 0 else '+' ))

		if - float(corMat[i][j]) > coreCut and float(pMat[i][j]) < pCut:
			#Species, KO, cor, p
		
			negResLst.append((corMat[0][j], pMat[i][0], corMat[i][j], pMat[i][j], '-' if float(corMat[i][j]) < 0 else '+' ))


with open (".".join([arg1[4:-4], str(coreCut) + '-' + str(pCut), ".extracts.out"]), 'w') as f:
	for i in resLst:
		f.write("	".join(i) + "\n")

with open (".".join([arg1[4:-4], str(coreCut) + '-' + str(pCut), ".neg_extracts.out"]), 'w') as f:
	for i in negResLst:
		f.write("	".join(i) + "\n")

with open (".".join([arg1[4:-4], str(coreCut) + '-' + str(pCut), ".pos_extracts.out"]), 'w') as f:
	for i in posResLst:
		f.write("	".join(i) + "\n")