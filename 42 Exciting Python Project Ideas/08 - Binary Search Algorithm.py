def search(myList, to_search):
    if search_(myList, to_search,0, len(myList)):
        return True
    else:
        return False

def search_(myList, to_search, min, max):
    if min >= max-1:
        return False

    if to_search > myList[(min+max)//2]:
        return search_(myList, to_search, (min+max)//2, max)
    elif to_search < myList[(min+max)//2]:
        return search_(myList, to_search, min, (min+max)//2)
    else:
        return True

thisList = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43]

if search(thisList, 100):
    print("It is in this list")
else:
    print("It is NOT in this list")