import random

deck = []
slots = []
for i in range(0,24):
    slots.append(i)
    deck.append(0)
    
i = 0
j = 1
i_cnt = 0
while i < 24:
    current = random.choice(slots)
    deck[current] = j
    slots.pop(slots.index(current))
    
    i_cnt+=1
    if i_cnt == 4:
        i_cnt = 0
        j+=1
    i+=1


print(deck)
