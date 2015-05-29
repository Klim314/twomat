from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import entropy
from scipy.spatial.distance import braycurtis

def test(lst1,lst2):
	print("PEARSON: ", str(pearsonr(lst1, lst2)))
	print("SPEARMAN: ", str(spearmanr(lst1, lst2)))
	print("BRAYCURTIS: ", str(braycurtis(lst1, lst2)))
	print("KULLMANLEIBER: ", str(entropy(lst1, lst2)))

sp1 = [317,12226,169,15506,1649,78924,36,5247,18,84];
sp2 = [2838,99,70,882,41756,9584,12626,914,784,118]

test(sp1, sp2)
print()
test(sp2, sp1)