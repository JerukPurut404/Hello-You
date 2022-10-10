import random
from time import sleep

try:
    from loading import Loading
except ImportError:
    print('This game requires the loading module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/loading/')
    sys.exit()

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

Weapon = {}
rupee = 200

def game_over(reason):
  print("\n" + reason)
  print("Game Over!")
  play_again()

def intro():
	clear()
	loader = Loading(100, 'installing all the things.', '+')
	for count in range(1, 99):
		loader.complete(count)
		sleep(0.2)
	loader = Loading(100)
	loader.complete(10)
	sleep(1)
	loader.complete(20)
	sleep(1)
	loader.complete(30)
	sleep(1)
	loader.complete(40)
	sleep(1)
	loader.complete(50)
	sleep(1)
	loader.complete(60)
	sleep(1)
	loader.complete(70)
	sleep(1)
	loader.complete(80)
	sleep(1)
	loader.complete(90)
	sleep(1)
	print("\nWelkom naar deze advontuurlijke text based game over nieuwkomer in hyrule.")
	sleep(1)
	print("\nJij zal tussen 3 wapens en 3 dorpen moeten kiezen.")
	sleep(1)

def option_start():
	print("Kies je wapen: 1. Boko-Knots, 2. Lizal-Tweetand, 3. Dwell")


intro()

