'''
dict = []

cnt = 0

current = input("" + str(cnt) + ": ")
dict.append(current)
while current != "":
    cnt+=1
    current = input("" + str(cnt) + ": ")
    dict.append(current)
'''

def str_numbers(string, i):
    list = []
    for j in range(i):
        list.append(string + str(j))

    return list

def arrange_list(list, i):


	
dict = ["15", "dog", "sinigang", "reading", "November", "18", "2020"]

print("Dictionary: ", end="")
print(dict)

ALL = []
for i in dict:
    list1 = str_numbers(i, 100)
    ALL.append(list1)

print(ALL)
print("Total: " + str(len(ALL)))
