import random

print("The Utility Deck")
print("\t1. Heal")
print("\t2.1. Tinker +1")
print("\t2.2. Tinker +2")
print("\t2.3. Tinker +3")
print("\t2.4. Tinker +4")
print("\t3. Bulwark")
print("\t4. Encourage")

Energy = 5
Health = 20
Enemy = 20
Gauge = 0
Player_Strikes = int(random.randrange(1,12))
Enemy_Strikes = int(random.randrange(1,12))

util_deck = []
for i in range(3):
    util_deck.append(random.randrange(1,5))

print("\n\nYour Cards: ")

cnt = 1
for i in util_deck:
    print(cnt, "- ", end="")
    if i == 1:
        print("Heal ")
    elif i == 2:
        print("Tinker +", end="")
        t_value = random.randrange(1,5)
        print(t_value)
    elif i == 3:
        print("Bulwark")
    elif i == 4:
        print("Encourage")
    cnt += 1

choice = int(input("Card to Play: "))
if choice == 1:
    Health = Health + (Health*0.20)
elif choice == 2.1:
    Gauge+= 1
elif choice == 2.2:
    Gauge+= 2
elif choice == 2.3:
    Gauge+= 3
elif choice == 2.4:
    Gauge+= 4
elif choice == 3:
    Player_Strikes = Player_Strikes + (Player_Strikes*0.20)
elif choice == 4:
    Enemy_Strikes = Enemy_Strikes - (Enemy_Strikes*0.20)

won = random.randrange(1,3)
print("In This Round, Player", won, "won")
if choice == 1:
    print("You Healed Yourself by 20%!")

if choice == 3:
    print("You Played the Bulwark Card...")
    if won == 1:
        print("\tIt didn't work since you won the battle")
    else:
        Enemy_Strikes -= (Enemy_Strikes*0.20)
        print("\tThe Enemy's Strikes Have Decreased by 20%!")
        
elif choice == 4:
    print("You played the Encourage Card...")
    if won == 1:
        Player_Strikes+= (Player_Strikes*0.20)
        print("\tYour Strikes Have Increased by 20%!")
    else:
        print("\tIt didn't work since you lost the battle")

if won == 1:
    print("Player 1 attacked Player 2 with", Player_Strikes,"strikes.")
    Enemy -= Player_Strikes
else:
    print("Player 2 attacked Player 1 with", Enemy_Strikes,"strikes.")
    Health -= Enemy_Strikes
    
print("\n\nCurrent Stats: ")
print("\tPlayer Health:", Health)
print("\tEnemy Health:", Enemy)
print("\tEnergy:", Energy)
print("\tAttack Gauge:", Gauge)
