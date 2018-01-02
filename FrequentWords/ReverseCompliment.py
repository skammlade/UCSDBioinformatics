# Reverse Complement Problem: Find the reverse complement of a DNA string.
#      Input: A DNA string Pattern.
#      Output: Pattern⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯Pattern¯, the reverse complement of Pattern.

# Sample Input:
# AAAACCCGGT

# Sample Output:
# ACCGGGTTTT

inputSequence = input("Sequence=")

reverseSequence = ''.join(reversed(inputSequence))

for letter in reverseSequence:
    if letter == 'A':
    	print('T', end="")
    elif letter == 'T':
    	print('A', end="")
    elif letter == 'C':
    	print('G', end="")
    elif letter == 'G':
    	print('C', end="") 