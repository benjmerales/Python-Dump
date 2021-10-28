array = [1,2,3,4,5]
a = 2

new_array = array[a:len(array)] + array[0:a]
print(new_array)