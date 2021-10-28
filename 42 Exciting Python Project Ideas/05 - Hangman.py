import random
dict = [{"General Place":"Quarantine Facility"} , {"Broadway" : "Alexander Hamilton"}, {"Movie": "Eternal Sunshine of the Spotless Mind"}, {"Famous Actors": "Scarlett Johanson"}]

R = random.randrange(0,4)
current = dict[R]

category = list(current.keys())[0]
word = list(current.values())[0].upper()

print("\t\t\t\tCategory: ", end="")
print(category)

correct_guess = []
incorrect_guess = []
lives_left = 5

def check_if_win(guess, correct):
    if guess == correct:
        print("\t\t\t>>>\tYOU WIN!\t<<<")
        return True
    return False
def check_if_lose(lives_left):
    if lives_left == 1:
        print("\t\t\t>>>\tGAME OVER\t<<<")
        return True
    return False

while True:
    print("\t\tLives left: ", lives_left)
    print("\t\tWord: ", end="")
    
    for i in word:
        
        if i in correct_guess:
            print(i, end=" ")
        else:
            if i == ' ':
                print(" ", end = " ")
            else:
                print("_", end=" ")

   
    print()

    # Basic Input
    letter = input("\t\tEnter a letter: ").upper()

    # Checks if letter is already inputted
    if letter in correct_guess or letter in incorrect_guess:
        print("You have already inputted this letter!")
        continue

    # Checks letter input
    if letter in word:
        correct_guess.append(letter)
        print("\t\t\t>>>\tYes you have guessed correctly\t<<<")

        display = ""
        for i in word:
            if i in correct_guess:
                display += i
            else:
                if i == ' ':
                    display += " "
                else:
                    display += "_"

        # Win Checker
        if check_if_win(display, word): break
    else:
        incorrect_guess.append(letter)
        print("\t\t\t>>>\tWrong!\t<<<")
        lives_left -= 1

    # Lose Checker
    if check_if_lose(lives_left): break
    
    
    
