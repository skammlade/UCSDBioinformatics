# Sample Input:
# GCGCG
# GCG

# Sample Output:
# 2


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

## remove promt text to pass Stepik input
# fullSequence = input("Input test sequence:")
# subsequence = input("Input subsequence:")

fullSequence = input()
subsequence = input()

print(occurrences(fullSequence, subsequence))

