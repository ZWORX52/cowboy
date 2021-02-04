from random import randint
import time
import sys
import keyboard

def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.35)

name = input("What is your name")

if name == "":
  name = "Player 1"

print("Hello " + name + "!" + "\n")

pScore = 0  
cScore = 0
pGun = 0
cGun = 0

delay_print(...)

while True:
  try: 
    chosen = radint(1,4)

    if chosen == 1:
      print("cmd chose to load")
      cGun = 1
    if chosen == 2:
      print("cmd chose to shield")
    if chosen == 3:
      print("cmd chose to mirror")
    if chosen == 4:
      print("cmd chose to fire")

    if chosen == 4 and cGun == 0:
      chosen =  randint(1,3)
       
    if keyboard.is_pressed('a'):
      print(name + " chose to load")
      pGun = 1
    if keyboard.is_pressed('s'):
      print(name + " chose to shield")
    if keyboard.is_pressed('d'):
      print(name + " chose to mirror")
    if keyboard.is_pressed('f'):
      print(name + " chose to fire")
      pGun = 0

  except:
    print("Try pressing A to load, S to shield, D to mirror, and F to fire.")
    break