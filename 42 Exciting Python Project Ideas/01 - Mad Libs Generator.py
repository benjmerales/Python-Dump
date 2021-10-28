'''

	There once was a hero named Ragnar(1) the Red(2) 
	Who came riding to Whiterun(3) from ole Rorikstead(4)
	And the braggart(5) did swagger and brandish his blade(6)
	As he told of bold battles and gold(7) he had made

	But then he went quiet, did Ragnar(1) the Red(2)
	when he met the shieldmaiden(8) Matilda(9) who said
	Oh, you talk(10) and you lie(11) and you drink(12) all our mead(13)
	Now I think it's high time that you lie down and bleed(14)

	And so then came clashing and slashing of steel(15)
	As the brave(16) lass Matilda(9) charged in full of zeal
	And the braggart(5) named Ragnar(1) was boastful(17) no more
	When his ugly(18) red(19) head rolled around on the floor

'''
import tkinter as tk
from functools import partial

def default_input(window, string):
    frame = tk.Frame(master=window, relief=tk.FLAT)
    w = tk.Label(master=frame, text=string)
    w.pack(side=tk.LEFT)
    w_entry = tk.Entry(master=frame)
    w_entry.pack(side=tk.LEFT)
    frame.pack()

    return w_entry

def print_story(words):
    print(
        f"""There once was a hero named {words[0].get()} the {words[1].get()} 
	Who came riding to {words[2].get()} from ole {words[3].get()}
	And the {words[4].get()} did swagger and brandish his {words[5].get()}
	As he told of bold battles and {words[6].get()} he had made

	But then he went quiet, did {words[0].get()} the {words[1].get()}
	when he met the {words[7].get()} {words[8].get()} who said
	Oh, you {words[9].get()} and you {words[10].get()} and you {words[11].get()} all our {words[12].get()}
	Now I think it's high time that you lie down and {words[13].get()}

	And so then came clashing and slashing of {words[14].get()}
	As the {words[15].get()} lass {words[8].get()} charged in full of zeal
	And the {words[4].get()} named {words[0].get()} was {words[16].get()} no more
	When his {words[17].get()} {words[18].get()} head rolled around on the floor
        """)
window = tk.Tk()
title = tk.Label(text="Mad Libs Generator v.0.1")
title.pack()
story_title = tk.Label(text="Story 1: A Hero")
story_title.pack()

w_1 = default_input(window, "Enter a name: ")
w_2 = default_input(window, "Enter an adjective: ")
w_3 = default_input(window, "Enter a place: ")
w_4 = default_input(window, "Enter another place: ")
w_5 = default_input(window, "Enter a general noun: ")
w_6 = default_input(window, "Enter an object: ")
w_7 = default_input(window, "Enter another object: ")
w_8 = default_input(window, "Enter a general noun: ")
w_9 = default_input(window, "Enter a name: ")
w_10 = default_input(window, "Enter a verb: ")
w_11 = default_input(window, "Enter another verb: ")
w_12 = default_input(window, "Enter ANOTHER verb: ")
w_13 = default_input(window, "Enter a general noun: ")
w_14 = default_input(window, "Enter a verb: ")
w_15 = default_input(window, "Enter a general noun: ")
w_16 = default_input(window, "Enter an adjective: ")
w_17 = default_input(window, "Enter another adjective: ")
w_18 = default_input(window, "Enter ANOTHER adjective: ")
w_19 = default_input(window, "Enter one last adjective: ")
words = [w_1,w_2,w_3,w_4,w_5,w_6,w_7,w_8,w_9,w_10,w_11,w_12,w_13,w_14,w_15,w_16,w_17,w_18,w_19]


submit = tk.Button(text = "Submit: ", command=partial(print_story,words))
submit.pack()
    
