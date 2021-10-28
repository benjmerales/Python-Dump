import random
import math
Player = 20
Enemy = 20
AttackPlayers = math.floor(random.randrange(1,13))
AttackEnemy = math.floor(random.randrange(1,13))

print("Available Frailty Deck:")
print("1. Overcharge")
print("2. Melancholy")
print("3. Break")
print("4. Hack")

frail_deck = []
for i in range(3):
    frail_deck.append(random.randrange(1,5))

print("\n\nYour Cards: ")

cnt = 1
for i in frail_deck:
    print(cnt, "- ", end="")
    if i == 1:
        print("Overcharge")
    elif i == 2:
        print("Melancholy")
    elif i == 3:
        print("Break")
    elif i == 4:
        print("Hack")
    cnt+=1

choice = int(input("Card to play: "))
if choice == 1:
    print("You played overcharge!")
    print("The enemy's attack gauge is", AttackEnemy)
    add_atkg = int(input("What will you add? [0,2,3] : "))
    AttackEnemy += add_atkg
elif choice == 2:
    AttackEnemy -= (AttackEnemy*0.20)
elif choice == 3:
    AttackPlayers += (AttackEnemy*0.20)
elif choice == 4:
    AttackEnemy += random.randrange(5,7)
print("\n\nIn this Round...")
if AttackEnemy > 12 :
    print("Player 2 has overcharged!")
    AttackEnemy = AttackPlayers - 1

if AttackPlayers > AttackEnemy:
    print("Player 1 wins")
    print("Player 1 attack Player 2 with", AttackPlayers - AttackEnemy, "strikes.")
    Enemy -= AttackPlayers-AttackEnemy
elif AttackEnemy > AttackPlayers:
    print("Player 2 wins")
    print("Player 2 attack Player 1 with", AttackEnemy - AttackPlayers, "strikes.")
    Player -= AttackEnemy - AttackPlayers
else:
    print("Draw!")

print("\n\nCurrent Stats: ")
print("\tPlayer Health:", Player)
print("\tEnemy Health:", Enemy)
print("\tCurrent Attack Gauge of Player:", AttackPlayers)
print("\tCurrent Attack Gauge of Enemy:", AttackEnemy)
