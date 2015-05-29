#generates test data of counts
#2d matrix withSamples at top, covariates at left
#toDo

import random, string

length, height = 10, 20

def gentest(length, height, codifier):
	
	temp = [codifier] + [''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(5)) for j in range(length)]
	holder = []
	holder.append(temp)
	for i in range(height):
		holder.append([codifier + ''.join(random.choice(string.digits+ '  ') for i in range(10))] + \
			[''.join(random.choice(string.digits) for i in range(random.randint(2,5))) for j in range(length)])
	return holder
first = gentest(length, height, "SP")
second = gentest(length, height+5, "KO")
second[0] = [i for i in first[0]]
second[0][0] = "KO"

third = gentest(length, height+5, "EC")
third[0] = [i for i in first[0]]
third[0][0] = "EC"

with open ("species.count", 'w') as f:
	for i in first:
		f.write("	".join(i) + '\n')

with open ("KO.count", 'w') as f:
	for i in second:
		f.write("	".join(i) + '\n') 
with open ("EC.count", 'w') as f:
	for i in third:
		f.write("	".join(i) + '\n') 