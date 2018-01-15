# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
#      Input: A DNA string Genome.
#      Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).

# Sample Input:
# TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

# Sample Output:
# 11 24

genome=input()

skew=0
skewDictionary = {}

for genomeBaseIndex, genomeBase in enumerate(genome):
# for base in genome:
	if genomeBase=="C":
		skew=skew - 1
	
	if genomeBase=="G":
		skew=skew + 1

	skewDictionary[genomeBaseIndex]: skew 

	# print(str(genomeBaseIndex) + "," + str(skew))

# print(min(dict, key=dict.get))
for i, j in skewDictionary.items():
	print(i,j)
