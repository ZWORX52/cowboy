from random import randint
import time
import sys
import keyboard

def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

name = input("What is your name")

if name == "":
  name = "Player"

delay_print("Hello " + name + "!" + "\n")

pScore = 0  
cScore = 0
pGun = 0
cGun = 0

while True:
  try: 
    delay_print("Welcome to cowboy! A duel to the death!! In this showdown you have four options: press A to load your gun, S to shield, D to mirror, or F to fire your gun...")
    
    delay_print("Hit ENTER and chose your move.")

    pChose = input()

    if keyboard.read_key() == "a":
      delay_print(name + " chose to load")
      pGun = 1
      pChose = 'load'
    if keyboard.read_key() == "s":      
      delay_print(name + " chose to shieldR")
      pChose = 'shield'
    if keyboard.read_key() == "d":
      delay_print(name + " chose to mirror")
      pChose = 'mirror'
    if keyboard.read_key() == "f":
      delay_print(name + " chose to fire")
      pGun = 0
      pChose = 'fire'

    delay_print("\nPress A,S,D, or F to trigger your opponent's response.")


    cChose = randint(1,4)

    if cChose == 1:
      delay_print("\nThe cmd chose to load\n")
      cChose = 'load'
      cGun = 1
    if cChose == 2:
      delay_print("\nThe cmd chose to shield\n")
      cChose = 'shield'
    if cChose == 3:
      delay_print("\nThe cmd chose to mirror\n")
      cChose = 'mirror'
    if cChose == 4:
      delay_print("\nThe cmd chose to fire\n")
      cChose = 'fire'
      cGun = 0

    if pChose == cChose:
      delay_print("And it's a draw!!!\n")
    elif pChose == 'fire' and cCHose == 'load':
      delay_print("The cmd has a bullet.....just not in his gun barrel! You win!!\n")
      pScore = pScore + 1
    elif pChose == 'mirror' and cChose == 'fire':
      delay_print("Just in time!!! You managed to deflect your death....\n")
      pScore = pScore + 1
    elif pChose == 'load' and cCHose == 'fire':
      delay_print("Oooo..that's gotta hurt. Sorry, but loading was a fatal mistake...\n")
      cScore = cScore + 1

    elif pChose == 'fire' and cChose == 'load':
      delay_print("Youcould have taken out that mirror any other time, but you chose now..\n") 
      cScore = cScore + 1
    else:
        delay_print("You both live for another day..")

    delay_print(name + "'s score is " + pScore)
    delay_print("\nThe cmd's score is " + cScore)

    break
  except:
    break