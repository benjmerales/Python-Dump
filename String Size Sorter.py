string = "The quick brown fox jumps over the lazy dog."

space_position = [string.find(' ') for i in string[string.find(' ')+1:]]
print(space_position)
