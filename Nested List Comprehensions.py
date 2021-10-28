def printM(matrix):
    for sublist in matrix:
        for index in sublist:
            print(index, end="  ")
        print('')

repeated_list_matrix = [ [1,2,3,4,5] for i in range(5) ]
printM(repeated_list_matrix)

flattened_matrix = [index for sublist in
                    [[1,2,3],[4,5,6],[7,8,9]]
                    for index in sublist]

print(flattened_matrix)
