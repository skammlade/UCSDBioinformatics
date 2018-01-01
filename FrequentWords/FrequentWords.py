# Sample Input:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4

# Sample Output:
# CATG GCAT

def get_all_k_mer(string, k=1):
   length = len(string)
   return [string[i: i+ k] for i in range(length-k+1)]

from collections import Counter

fullSequence = input()
kmerSize = input()

x = Counter(get_all_k_mer(fullSequence, k=int(kmerSize)))

maxval = max(x.values())

for key, value in x.items():
	if value == maxval:
		print(key, end=" ")
