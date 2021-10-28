a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
            print("Equilateral")
    elif a == b or a == c or b==c:
            print("Isosceles")
    elif a + b == c or b + c == a or  a + c == b :
            print("Degenerate Triangle")
    else:
            print("Scalene Triangle")
else:
    print("Invalid")