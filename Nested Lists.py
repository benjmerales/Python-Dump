if __name__ == '__main__':
    MS = [['Harry', 37.21], ['Cherry',37.21], ['Tina',37.2], ['Akriti', 41], ['Harsh', 39]]

    MS2 = [i for i in MS if i[1] != min([row[1] for row in MS])]
    print(MS)
    print(MS2)

    names = [ i[0] for i in MS2 if i[1] == min(row[1] for row in MS2)]

    print(names)
