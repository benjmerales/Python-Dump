print("Enter up to how many numbers: ", end="")
i = int(input())
print("Enter how many numbers in a set: ", end="")
j = int(input())

cnt = 0
num = 1
set_cnt = int(i/j)
rem = i % j
print("Total # of Numbers w/o sets: ", rem) 
print("Number of sets available:", set_cnt)
while cnt < set_cnt:
    set_elem = "[ "
    sum_ = 0
    j_cnt = 0
    while j_cnt < j:
        set_elem += str(num)+ ","
        sum_ += num
        j_cnt += 1
        num += 1
    print(set_elem, "]")
    print("Sum of Set", cnt+1, ":", sum_)

    cnt+=1
    
current = i - rem + 1
set_elem = "[ "
sum_ = 0
while current <= i:
    set_elem += str(current) + ", "
    sum_+=current
    current +=1
    
if rem != 0:
    print(set_elem, "]")
    print("Remaining sum: ", str(sum_))
