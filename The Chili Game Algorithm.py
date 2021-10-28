candies = 13
chilis = 1

turn = 1
while candies != 0:
    take = int(input("Player " + str(turn%2 + 1) + " takes "))
    print("candies")
    candies -= take
    print(candies, " candies remaining...\n")
    take = 4
    print("Computer takes ", take, " candies")
    print(candies, " candies remaining...\n")
