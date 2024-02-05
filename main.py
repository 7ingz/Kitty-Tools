from scripts.sprint import sprint
from subprocess import call
import time
import os
from os import system
os.system('git clone https://github.com/CPScript/Kitty-Tools') # update

# clear Terminal:
os.system('clear')

# Old "clear terminal" before my silly self realized i can use "os.system('clear')"
# puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
# if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'): 
#    delet = 'cls'
#    dr = '\\' 
#else:
#    delet = 'clear' 
#    dr = '/' 
#os.system(delet) 

# tui
print(f"|======= News =======| ")
print(f" News: we'll be right back with that!")
print(f" Note: *STAR* this repo so I can get more support :p")
print(f"|====================| ")
time.sleep(4) 

# clear the Termianl
os.system('clear')


print(f">| Kahoot Answer Client ||<")
print(" ")
print(f"--------------------")
print(f"/1/ How to use | Shows you how to use the tool")
print(f"/2/ Information | Credits, licence, and more")
print(f"/3/ Flooder | Flood a Kahoot game (Getting Updated!)")
print(f"/4/ Answer Hack | Start the answer client")
print(f"--------------------")
choice = input("Make Number Selection :")


if choice == "1":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/HTU.py"])

if choice == "2":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/Info.py"])

if choice == "3":
    print(" ")
    print("Loading...")
    time.sleep(1)
    call(["python", "Kahoot/flood/Info.py"])

if choice == "4":
    print(" ")
    print("Starting...")
    time.sleep(1)
    print("\n" * 64)  # imma this makes more sense
    call(["python", "Kahoot/kahoot.py"])

time.sleep(25)
print(" ")
print("Program Made by 7inngz")

