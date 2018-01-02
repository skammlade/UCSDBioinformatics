# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#      Input: Two strings, Pattern and Genome.
#      Output: All starting positions where Pattern appears as a substring of Genome.

# Sample Input:
# ATAT
# GATATATGCATATACTT

# Sample Output:
# 1 3 9

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

pattern = input("Pattern=")
sequence = input("Sequence=")

countOccurrences = occurrences(sequence, pattern)

# # Find first index of this string.
# i = sequence.find(pattern)
# print(i)

# # Find first index (of this string) after previous index.
# b = sequence.find(pattern, i + 1)
# print(b)

i = sequence.find(pattern)
for i in range(i, countOccurrences):
	print(i)
	# index = sequence.find(pattern, i + 1)
	# print(index, end="")
	# i = index

i = sequence.find(pattern)
while count < (countOccurrences + 1):
	b = sequence.find(pattern, i + 1)
	count += 1