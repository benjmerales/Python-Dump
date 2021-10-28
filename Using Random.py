import random

tried = []

cnt = 0

min = 1
max = 5

tried.append(random.randrange(min,max))
while cnt < max-1:
    current = random.randrange(min,max)
    if current not in tried:
        tried.append(current)
        cnt += 1

print(len(tried))
