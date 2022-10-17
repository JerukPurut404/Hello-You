import random
from time import sleep

try:
    from loading import Loading
    from easy_stopwatch import Stopwatch
except ModuleNotFoundError as e:
	modulename = str(e).split("No module named ")[1].replace("'", "")
	input(f"Please install module with: pip install {modulename}")
	exit()

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_yes = ["Y", "y", "yes"]
answer_no = ["N", "n", "no"]

landgoed = []
weapon = []
dorp = []
rupee = 200
stopwatch = Stopwatch()

def game_over(reason):
  print("\n" + reason)
  print("Game Over!")
  stopwatch.stop()
  print("Jouw tijd is " + str(stopwatch.time()))
  play_again()

def play_again():
  print("\nWil je nog een keer spelen? (y of n)")
  answer = input(">")
  if answer in answer_yes:
  	option_start()
  elif answer in answer_no:
    exit()
  else:
  	print("Alsjeblieft typt yes of no")
  	play_again()

def intro():
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
	print("\nHet doel is om een huis te hebben en te overleven")
	print("\nJij zal tussen 3 wapens en 3 dorpen moeten kiezen.")
	sleep(1)
	option_start()

def option_start():
	stopwatch.start()
	print("Kies je wapen: 1. Boko-Knots, 2. Lizal-Tweetand, 3. Dwell. Type het nummer graag. ")
	option = input(">")
	if option == "1":
		weapon.append("Boko-Knots")
		weapon.append(random.randrange(1,20))
		print("Jij hebt gekozen voor Boko-Knots")
		print("Jouw wapen is " + weapon[0], "en jouw wapen sterkte is " + str(weapon[1]))
		option_dorp()
	elif option == "2":
		weapon.append("Lizal-Tweetand")
		weapon.append(random.randrange(1,100))
		print("Jij hebt gekozen voor Lizal-Tweetand")
	elif option == "3":
		weapon.append("Dwell")
		weapon.append(random.randrange(1,11))
		print("Jij hebt gekozen voor dwell")
	else:
		game_over("jij kan geen nummer typen of zo?")

def option_dorp():
	print("JIj kan kiezen tussen 3 dorpen: 1. Hateno, 2. Gerudo Town, 3.Lurelin viliage.")
	option = input(">")
	if option == "1":
		dorp.append("Hateno")
		print("Jij hebt gekozen voor Hateno")
		dorp_hateno()
	elif option == "2":
		dorp.append("Gerudo Town")
		print("Jij hebt gekozen voor Geurdo Town")
		dorp_gerudotown()
	elif option == "3":
		dorp.append("Lurelin viliage")
		print("Jij hebt gekozen voor lurelin viliage")
		dorp_lurelinviliage()
	else: 
		game_over("Jij kan echt geen nummer typen of zo?")

def dorp_hateno():
	print("Je kan een landgoed kiezen tussen A.High Ground, B.Firly Pond en C.Zeikoa Pond. What kiest je? A,B,C")
	option = input(">")
	if option in answer_A:
		landgoed.append("High Ground")
		print("Jij hebt gekozen voor High Ground")
		enemy_incoming_high_ground()
	elif option in answer_B:
		landgoed.append("Firly Pond")
		print("Jij hebt gekozen voor Firly Pond")
		enemy_incoming_fp()
	elif option in answer_C:
		landgoed.append("Zeikoa Pond")
		print("Jij hebt gekozen voor Zeikoa Pond")
		enemy_incoming_zp()
	else:
		dorp_hateno()

def enemy_incoming_high_ground():
	bokolins = random.randrange(1,30)
	print("Jij komt gemeene bokoblins tegen met de health van "+ str(bokolins),". Ze komen dichterbij naar je richting toe. Je hebt je wapen bij je. Wat zou je doen? A. Vechten, B. Rennen, C.Schreeuwen")
	print("Jij kan tegen de bokolins vechten of je kan rennen, Wat zou je doen?")
	option = input(">")
	if option in answer_A:
		if weapon[1] > bokolins:
			story_nachtronde()
		else:
			game_over("Helaas jij heeft verloren van bokolins")
	elif option in answer_B:
		print("Jij hebt gekozen voor Rennen")
		story_rennen()
	elif option in answer_C:
		game_over("Jij hebt gekozen voor Schreeuwen maar dat helpt niet.")


def enemy_incoming_fp():
	lizalfos = random.randrange(1,40)
	print("Jij wilt even rusten in de pond en ga een beetje zwemmen maar je komt lizalfos tegen met de health van "+ str(lizalfos),". Wat zou je doen? A. Vechten, B. Rennen, C.Schreeuwen")
	option = input(">")
	if option in answer_A:
		if weapon[1] > lizalfos:
			story_nachtronde()
		else:
			game_over("Helaas jij heeft verloren van lizalfos")
	elif option in answer_B:
		print("Jij hebt gekozen voor Rennen")
		story_rennen()
	elif option in answer_C:
		game_over("Jij hebt gekozen voor Schreeuwen maar dat helpt niet.")

def enemy_incoming_zp(): 
	lizalfos = random.randrange(1,40)
	print("Jij wilt even rusten in de pond en ga een beetje zwemmen maar je komt lizalfos tegen met de health van "+ str(lizalfos),". Je kijkt even naar links en je vindt een roestig slagzwaard. A. Vechten met je huidige wapen, B. Vechten met roestige slagzwaard, C.Schreeuwen")
	option = input(">")
	if option in answer_A:
		if weapon[1] > lizalfos:
			story_nachtronde()
		else:
			game_over("Helaas jij heeft verloren van lizalfos")
	elif option in answer_B:
		weapon.append("roestige slagzwaard")
		weapon.append(random.randrange(1,15))
		if weapon[3] > lizalfos:
			option_roestig_slagzwaard()
		else:
			game_over("Helaas is je roestige slagzwaard niet sterk genoeg om te vechten")
	elif option in answer_C:
		game_over("Jij hebt gekozen voor Schreeuwen maar dat helpt niet")

def story_nachtronde():
	print("Jij heeft gevochten en het is je gelukt om hun te doden. Je vertelt de mensen over de gebeurtenis. Ze zeggen dat ze zal een Nachtrondes gehouden en ze kozen je om te doen. Wat zou je zeggen?")
	print("A. Nee, ik wil het niet, ik ben bang.")
	print("B. Ja hoor, ik zal het doen.")
	print("C. Ik weet het niet, beslist jullie maar.")
	option = input(">")
	if option in answer_A:
		option_giveup()
	elif option in answer_B:
		option_work_nachtrondes_zonder_harnas()
	elif option in answer_C:
		if random.randint(1,2)==1:
			option_giveup()
		else:
			option_work_nachtrondes_zonder_harnas()


def story_rennen():
	print("jij rent naar Hateno Ancient Tech Lab en ze zeggen dat ze kan een harnas bouwen maar als je een moer kunnen vinden en daarna kun je werken aan Nachtrondes. Wat zou je doen?")
	print("A.'Ja ik zal het vinden voor de harnas'")
	print("B.'Nee ik kan die nachtronde doen zonder dat harnas'")
	print("C.'Ik ga niet op de nachtrondes werken en ik hoeft ook die harnas niet'")
	option = input(">")
	if option in answer_A:
		option_work_nachtrondes_met_harnas()
	elif option in answer_B:
		option_work_nachtrondes_zonder_harnas()
	elif option in answer_C:
		option_giveup()
def option_roestig_slagzwaard():
	print("Jij vecht maar je breek je zwaard. Je bent naar de mensen te vragen of ze een nieuwe wapen kunnen maken. Een wapenmaker zegt dat hij kan je een nieuwe zwaard maken maar je moet de nachtrondes doen. Wat zou je zeggen?")
	print("A. 'Ok, daar ga ik mee akkord'")
	print("B. 'Nee, Ik wil het niet. bedankt'")
	print("C. 'Ik denk dat ik ook een harnas nodig voor veiligheid voor die werk.'")
	option = input(">")
	if option in answer_A:
		option_work_nachtrondes_zonder_harnas()
	elif option in answer_B:
		option_giveup()
	elif option in answer_C: 
		option_work_nachtrondes_met_harnas()
def option_giveup():
	game_over("Je gave de werk aan iemand anders. Uiteindelijk je hebt krijg werk in verfwinkel en een huis.")
def option_work_nachtrondes_zonder_harnas():
	game_over("Je hebt helaas moeten veel monster slachten in de nacht. Het is ten koste van je leven. Ze bouwen een monument voor je. ")
def option_work_nachtrondes_met_harnas():
	game_over("Je heeft alle monster slachten door de nacht heen. Je krijgt een beloning een huis en een vaste baan. Ze bouwen een monument voor je ook. ")

intro()