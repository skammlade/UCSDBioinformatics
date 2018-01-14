# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#      Input: Two strings, Pattern and Genome.
#      Output: All starting positions where Pattern appears as a substring of Genome.

# Sample Input:
# ATAT
# GATATATGCATATACTT

# Sample Output:
# 1 3 9

pattern = input()
genome = input()
# print(genome[0:len(genome)-len(pattern)+1])
for genomeBaseIndex, genomeBase in enumerate(genome[0:len(genome)-len(pattern)+1]):
    match = True
    
    for patternBaseIndex, patternBase in enumerate(pattern):
        
        # print(str(patternBaseIndex) + ':' + patternBase + '\n')
        # print(str(genomeBaseIndex) + ':' + genomeBase + ' ')
        # if genomeBaseIndex + patternBaseIndex >= len(genome):
        #     match = False
        #     break
        
        if patternBase != genome[genomeBaseIndex + patternBaseIndex]:
            match = False
            break

    if match:
        # print("match found at: " + str(genomeBaseIndex))
        print(genomeBaseIndex, end=" ")

