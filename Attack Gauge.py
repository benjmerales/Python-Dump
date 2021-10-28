import random

attack_gauge_player1 = 0
attack_gauge_player2 = 0

standing_player1 = 0
standing_player2 = 0

health_points_player1 = 20
health_points_player2 = 20

energy_points_player1 = 5
energy_points_player2 = 5

turn = 0

while True:

#prompts which player's turn is it
    if turn % 2 == 0:
        print("It is player ONE's turn...")
    else:
        print("It is player TWO's turn...")

#current player chooses to hit or stand
    choice = input("Hit or Stand: ")
    if choice.upper() == 'H':
        card = random.randrange(1,7)
        if turn % 2 == 0:
            attack_gauge_player1 += card
        else:
            attack_gauge_player2 += card
            
    elif choice.upper() == 'S':
        if turn % 2 == 0:
            standing_player1 = 1
        else:
            standing_player2 = 1
        print("I stand my ground!")

    print("My current Attack Gauge is ", end="")
    if turn % 2 == 0:
        print(attack_gauge_player1)
        if attack_gauge_player1 > 12:
            print("WARNING! Overcharged!")
            attack_gauge_player1 = attack_gauge_player2 - 1
            standing_player1 = 1
    else:
        print(attack_gauge_player2)
        if attack_gauge_player2 > 12:
            print("WARNING! Overcharged!")
            attack_gauge_player2 = attack_gauge_player1 - 1
            standing_player2 = 1
    input("Press enter to end turn\n")

    if standing_player1 and standing_player2:
        print("Both Players have standed their ground! Calculating Battle Score.")
        if attack_gauge_player1 > attack_gauge_player2:
            strikes = attack_gauge_player1 - attack_gauge_player2
            print("Player One has won the Round!")
            print("Player Two will then take", strikes, "strikes from player One")
            health_points_player2 -= strikes
        elif attack_gauge_player1 < attack_gauge_player2:
            strikes = attack_gauge_player2 - attack_gauge_player1
            print("Player Two has won the Round!")
            print("Player One will then take", strikes, "strikes from player Two")
            health_points_player1 -= strikes
        else:
            print("Draw! Both Players will get five energy points")
        if health_points_player1 == 0 or health_points_player2 == 0:
            if health_points_player1 == 0:
                print("Player 2 Wins!")
            else:
                print("Player 1 Wins!")
            break

    turn+=1












    
