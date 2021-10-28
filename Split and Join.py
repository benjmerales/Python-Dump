def split_and_join(line):
    # write your code here
    linelist = line.split()
    joinline = "-".join(linelist)

    return joinline
if __name__ == '__main__':
    str = input("Input: ")
    print("Result:", split_and_join(str))
