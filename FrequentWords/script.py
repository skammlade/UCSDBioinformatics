def get_all_k_mer(string, k=1):
   length = len(string)
   return [string[i: i+ k] for i in range(length-k+1)]

# Then you can use collections.Counter to count the repetition of each k-mer:

from collections import Counter

with open('FrequentWordsData.txt', 'r') as content_file:
    s = content_file.read()
# s = 'GATCCAGATCCCCATAC'
for i in range(2, 10):
	x = Counter(get_all_k_mer(s, k=i))

# y = get_all_k_mer(s, k=2)

	print(x)