n = int(input())
binary = ""
while n > 0:
    binary += str(n%2)
    n = n // 2

binary = binary[::-1]
MaxO = 0
current_cnt = 0
print(binary)
for i in binary:
    if i is '0':
        if current_cnt > MaxO:
            
            MaxO = current_cnt
        current_cnt = 0
    else:
        current_cnt+= 1
if current_cnt > MaxO:
    MaxO = current_cnt
print("The Maximum number of consecutive ones are: ", MaxO)
