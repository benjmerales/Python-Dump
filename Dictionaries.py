dictionary = {"Dog" : "Wambo", "Puppy" : "Tsukki", "Cat" : "Mingming"}
print(dictionary)

print(*dictionary) # prints keyword in a single line

for i in dictionary: # prints keywords by line
    print(i)

for i in dictionary: # prints values
    print(dictionary[i])

for i in dictionary.values(): # prints values
    print(i)


