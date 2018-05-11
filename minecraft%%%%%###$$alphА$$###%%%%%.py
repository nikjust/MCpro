import os

import time

print("""
XX
 XX        X  X
 XXX      XX         X    X
 X XX    XXX         XX   X        XX
 X  X   XXXX  X      XX  XX        XXXXXXX    craft
 X   X XX X   X      XXX X         X          craft
 X   XX   X   X      X X X        XX   XXX    craft
XX        X   X      X XXXX       X XXXX      craft
X         X   X      X  XXX       X           craft
              X      X   XX       XXXXXXX     craft
""")
time.sleep(5)
print("""
                    XX
  X                XXX     X
  X              XX  X    XX    X   X XXX      XX   XX
  X             XX   X   X     XX   XXX X     X  X  X
 X             XXXX  X  XX    XX    X   X    X     XX
 X            XX   XXX XX    XX     X   X   XX     XXX
XX          XX       X X    XX     XX   X   X     XX X
XX        XX         X XXXXX       XX       XXXXXXX  X
  XXX    XX          X                           XX  X
         X

 by: nik just
 lite version
 alpha 1
""")
print ("1-legacy 2-new")
b = input()
if b == "1":
    os.startfile("C:\\McP1.exe")
elif b == "2":
    os.startfile("C:\\tlauncher-2.23_beta.exe")

elif b == "?":
    print("wrong!!!")
else:
    print("не то")
    


