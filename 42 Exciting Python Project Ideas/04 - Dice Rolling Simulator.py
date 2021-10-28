import tkinter as tk
from functools import partial
import random

def roll_dice():
    diceN = random.randrange(1,7)
    print("You rolled a " + str(diceN))
    return diceN

def draw_dice(dice):
    dice.delete("all")
    
    number = roll_dice()
    if(number == 1):
        dice.create_oval(35,35,60,60, fill="black")
    if(number == 2):
        dice.create_oval(15,15,30,30, fill="black")
        dice.create_oval(60,60,80,80, fill="black")
    if(number == 3):
        dice.create_oval(15,15,30,30, fill="black")
        dice.create_oval(60,60,80,80, fill="black")
        dice.create_oval(40,40,55,55, fill="black")
    if(number == 4):
        dice.create_oval(10,10,30,30, fill="black")
        dice.create_oval(10,70,30,90, fill="black")
        dice.create_oval(70,10,90,30, fill="black")
        dice.create_oval(70,70,90,90, fill="black")    
    if(number == 5):
        dice.create_oval(10,10,30,30, fill="black")
        dice.create_oval(10,70,30,90, fill="black")
        dice.create_oval(70,10,90,30, fill="black")
        dice.create_oval(70,70,90,90, fill="black")
        dice.create_oval(37,37,55,55, fill="black")
        
    if(number == 6):
        dice.create_oval(10,10,30,30, fill="black")
        dice.create_oval(10,70,30,90, fill="black")
        dice.create_oval(70,10,90,30, fill="black")
        dice.create_oval(70,70,90,90, fill="black")
        dice.create_oval(10,40,30,55, fill="black")
        dice.create_oval(70,40,90,60, fill="black")

    dice.pack()
window = tk.Tk()
dice = tk.Canvas(bg="white", height=100, width=100)

dice.pack()

rollButton = tk.Button(text="Roll", command=partial(draw_dice, dice))
rollButton.pack()
window.mainloop()
