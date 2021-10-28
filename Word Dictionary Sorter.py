
#words = input("Words: ").split(' ')
words = "the quick brown fox jumps over the lazy dog".split(' ')
print(words)

sortedWords = []
i = 0
sequence = [][]
for aWord in words:
	j = 0 
	for letter in aWord:
		sequence[i][j] = letter
		j+=1
	i+=1

