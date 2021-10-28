print("Paragraph:")
Paragraph = input()

Sentences = Paragraph.split('.')

words = input("Words: ").split(' ')

contains = []

for sentence in Sentences:
    if words[0] in sentence or words[1] in sentence:
        contains.append(sentence)

for i in contains:
    print(i)
