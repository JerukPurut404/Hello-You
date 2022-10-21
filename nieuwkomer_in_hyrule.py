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
rupee = ['200']
stopwatch = Stopwatch()

def game_over(ending, reason):
  print("\n" + ending)
  print("\n" + reason)
  print("Game Over!")
  stopwatch.stop()
  print("Jouw tijd is " + str(stopwatch.time()))
  print("Jouw rupee is " + rupee[0])
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
	print("\nHet doel van de game is dat je een huis en werk hebt in de gekozen dorp")
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
		option_dorp()
	elif option == "3":
		weapon.append("Dwell")
		weapon.append(random.randrange(1,11))
		print("Jij hebt gekozen voor dwell")
		option_dorp()
	else:
		option_start()

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
		option_dorp()

# Hateno

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
			game_over("Bad Ending","Helaas jij heeft verloren van bokolins")
	elif option in answer_B:
		print("Jij hebt gekozen voor Rennen")
		story_rennen()
	elif option in answer_C:
		game_over("Bad ending", "Jij hebt gekozen voor Schreeuwen maar dat helpt niet.")


def enemy_incoming_fp():
	lizalfos = random.randrange(1,40)
	print("Jij wilt even rusten in de pond en ga een beetje zwemmen maar je komt lizalfos tegen met de health van "+ str(lizalfos),". Wat zou je doen? A. Vechten, B. Rennen, C.Schreeuwen")
	option = input(">")
	if option in answer_A:
		if weapon[1] > lizalfos:
			story_nachtronde()
		else:
			game_over("Bad ending","Helaas jij heeft verloren van lizalfos")
	elif option in answer_B:
		print("Jij hebt gekozen voor Rennen")
		story_rennen()
	elif option in answer_C:
		game_over("Bad ending","Jij hebt gekozen voor Schreeuwen maar dat helpt niet.")

def enemy_incoming_zp(): 
	lizalfos = random.randrange(1,40)
	print("Jij wilt even rusten in de pond en ga een beetje zwemmen maar je komt lizalfos tegen met de health van "+ str(lizalfos),". Je kijkt even naar links en je vindt een roestig slagzwaard. A. Vechten met je huidige wapen, B. Vechten met roestige slagzwaard, C.Schreeuwen")
	option = input(">")
	if option in answer_A:
		if weapon[1] > lizalfos:
			story_nachtronde()
		else:
			game_over("Bad ending", "Helaas jij heeft verloren van lizalfos")
	elif option in answer_B:
		weapon.append("roestige slagzwaard")
		weapon.append(random.randrange(1,15))
		if weapon[3] > lizalfos:
			option_roestig_slagzwaard()
		else:
			game_over("Bad ending","Helaas is je roestige slagzwaard niet sterk genoeg om te vechten")
	elif option in answer_C:
		game_over("Bad ending", "Jij hebt gekozen voor Schreeuwen maar dat helpt niet")

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
	game_over("Neutral Ending","Je gave de werk aan iemand anders. Uiteindelijk je hebt krijg werk in verfwinkel en een huis.")
def option_work_nachtrondes_zonder_harnas():
	game_over("Bad ending", "Je hebt helaas moeten veel monster slachten in de nacht. Het is ten koste van je leven. Ze bouwen een monument voor je. ")
def option_work_nachtrondes_met_harnas():
	game_over("Good ending", "Je heeft alle monster slachten door de nacht heen. Je krijgt een beloning een huis en een vaste baan. Ze bouwen een monument voor je ook. ")

# Gerudo Town

def dorp_gerudotown():
	print("Jij hebt een meisje kleding nodig omdat gerudo is een vrouwen drop. Je hebt geen meisjes kleiding dus je hebt een keuze om eerst te werken of meteen de kleding kopen?")
	print("A. Werken")
	print("B. Meteen kopen - 200 rupee")
	print("C. Geeft het op")
	option = input(">")
	if option in answer_A:
		option_work_buiten_gerudotown()
	elif option in answer_B:
		rupee2 = int(rupee[0])
		if rupee2 > 200:
			option_huis()
		else:
			print("Sorry, jij hebt niet genoeg rupee")
			dorp_gerudotown()
	elif option in answer_C:
		game_over("Bad ending","Zelfmoord huh?")

def option_enter_town():
	print("Je komt de koningin Riju tegen, je zegt dat een woning zoek en ook werk. De koningin zegt dat je moet eerst werken om een huis te kopen. Wat wil je?")
	print("A. Werken")
	print("B. Meteen Huis kopen")
	print("C. Geeft het op")
	option = input(">")
	if option in answer_A:
		option_asiel()
	elif option in answer_B:
		if rupee2 > 200:
			option_huis()
		else:
			print("Sorry, jij hebt niet genoeg rupee")
			option_enter_town()
	elif option in answer_C:
		game_over("Bad ending", "Zelfmoord huh?")

def option_work_buiten_gerudotown():
	print("Je moet werken buiten de dorp en dat is op een oase gebied. Je krijgt de taak om kokosnoot op te halen bij de boom. Wat zou je doen ?")
	print("A. Doe het werk maar zonder veiligheidsmaatregelen")
	print("B. Hetzelfde maar met veiligheidsmaatregelen")
	print("C. Ik ga niet werken")
	option = input(">")
	if option in answer_A:
		game_over("Bad ending", "Jij bent een idiot door je nalatigheid")
	elif option in answer_B:
		rupee2 = int(rupee[0])
		rupee2 += 200
		print(rupee)
		option_enter_town()
	elif option in answer_C:
		game_over("Bad ending", "Zelfmoord huh?")

def option_asiel():
	print("Jij hebt geen huis nog, maar jij hebt nu werk dus dat is prima. Je zit nu in een soort van asiel opvang. Maar je werk als dierverzorger en je hebt een dier kwijt. Wat ga je doen?")
	print("A. Zeg tegen je baas dat je de dier kwijt hebt")
	print("B. Je zoekt de dier terug")
	print("C. Niet zeggen tegen je baas en ook niet zoeken")
	option = input(">")
	if option in answer_A:
		option_fired()
	elif option in answer_B:
		option_animal()
	elif option in answer_C:
		game_over("Bad ending", "Jij bent helaas uit het drop gezet vanwege luiheid")

def option_fired():
	print("Jij bent je baan kwijt maar je kan het terugverdienen door de dier te vinden. Wat zou je doen?")
	print("A. Zoek de dier weer terug")
	print("B. Koop een andere dier in plaats")
	print("C. Werk bij een andere baan")
	option = input(">")
	if option in answer_A:
		option_animal()
	elif option in answer_B:
		option_animal_fake()
	elif option in answer_C:
		option_work()

def option_animal_fake():
	print("Jij koopt een andere dier in plaats van de dier zoeken. Je baas is er in getrapt. Nu hebt kan je een huis kopen. Ga je hier huis kopen of niet? J of N? ")
	option = input(">")
	if option in answer_yes:
		option_house()
	elif option in answer_no:
		game_over("bad ending", "Jij bent helaas dakloos")

def option_house():
	print("Gelukt, Jij hebt de dier gevonden en jij krijgt je eerste salaris. Jij kan nu een huis betalen. Niet alle huizen zijn gelijk dus je kan kiezen? Wat wil je?")
	rupee[0] += 200 
	print("Jouw geld is nu " + rupee)
	print("A. Een huis met goede isolatie - 200")
	print("B. Een huis met slechte isolatie - 100")
	print("C. Maakt niks uit")
	option = input(">")
	if option in answer_A:
		rupee2 = int(rupee[0])
		if rupee2 > 200:
			rupee -= 200
			game_over("Good ending", "Jij hebt een goede leven gehad in Gerudo, stabiele inkomen met een goede huis")
		else:
			print("Sorry jij hebt niet genoeg rupee")
			option_house()
	elif option in answer_B:
		rupee2 = int(rupee[0])
		if rupee2 > 200:
			rupee -= 200
			game_over("Bad ending", "Jouw huis is niet sterk genoeg om te overleven en jij hebt niet een stabiele inkomenen")
		else:
			print("Sorry jij hebt niet genoeg rupee")
			option_house()
	elif option in answer_C:
		if random.randint(1,2)==1:
			rupee2 = int(rupee[0])
			if rupee2 > 200:
				rupee -= 200
				game_over("Good ending", "Jij hebt een goede leven gehad in Gerudo, stabiele inkomen met een goede huis")
			else:
				print("Sorry jij hebt niet genoeg rupee")
				option_house()
		else:
			rupee2 = int(rupee[0])
			if rupee2 > 200:
				rupee -= 200
				game_over("Bad ending", "Jouw huis is niet sterk genoeg om te overleven en jij hebt niet een stabiele inkomenen")
			else:
				print("Sorry jij hebt niet genoeg rupee")
				option_house()

# Lurelin 

def dorp_lurelinviliage():
	print("Het is een prachtige strand dorp. Alles kunt je hier vinden. Je wilt eerst hier een werk zoeken. Wat voor werk zoek je?")
	print("A. Visser worden")
	print("B. Hotel Medewerker worden")
	print("C. Boot verhuurder worden")
	option = input(">")
	if option in answer_A:
		option_visser()
	elif option in answer_B:
		option_hotel_medewerker()
	elif option in answer_C:
		option_boot_verhuurder()

def option_visser():
	rupee[0] += 100
	print("Jij hebt de werk als visser aangenomen en jij hebt je aller eerste vis gepakt. Wat zou je doen?")
	print("A. Verkoopt het aan lokale markt")
	print("B. Eet het lekker zelf op")
	print("C. Gooi het terug naar de zee")
	option = input(">")
	if option in answer_A:
		option_markt()
	elif option in answer_B:
		game_over("Bad ending", "Je hebt genoeg eten voor dat dag maar je krijgt geen geld en daardoor kan je niet een huis bouwen en ben je dakloos")
	elif option in answer_C:
		option_sea()

def option_hotel_medewerker():
	rupee[0] += 100
	print("Jij bent nu een hotel medewerker en een van je klant vroegt of je haar portefeuille gezien heeft. Je weet dat een collega heeft het gestolen. Wat zou je doen?")
	print("A. Geef het door aan de klant dat jij weet wie heeft het gestolen")
	print("B. Lieg tegen de mevrouw dat je het niet weet")
	print("C. Niks verder zeggen")
	option = input(">")
	if option in answer_A:
		game_over("Good ending", "Jij vertelt tegen de klant dat je weet welke collega die haar portefeuille gestolen heeft en je krijgt geld beloning,vaste baan en ook een huis")
		rupee[0] += 1000
	elif option in answer_B:
		game_over("Bad ending", "Jij heeft de klant niet verteld over je collega die de portefeuille gestolen heeft, de volgende dag het is bekend dat je collega heeft portefeuilie gestolen en hij geeft de schuld aan jou. En jij kan niet ermee weg.")
	elif option in answer_C:
		game_over("Neutral ending", "Jij werkt nog en krijg een huis maar verder geen beloning")

def option_boot_verhuurder():
	rupee[0] += 100
	print("Jij bent nu boot verhuurder, Jij heeft nu een boot verhuurt aan een klant maar na 15 minuten de boot lekte. Wat zou je doen?")
	print("A. Vroeg iemand om te komen helpen")
	print("B. Zwem naar hun toe en de lek herstelen")
	print("C.Niks doen")
	option = input(">")
	if option in answer_A:
		game_over("Bad ending", "De klant is al in de zeebodem toen je aan het hulp roepen. Jij bent gewoon je baan kwijt en dakloos")
	elif option in answer_B:
		game_over("Good ending", "Gelukkig je kan hun redden binnen de tijd, je krijgt beloning en je kan huis kopen nu.")
	elif option in answer_C:
		game_over("Bad ending", "Jij bent uit het land gezet door je nalatigheid")
	

def option_sea():
	print("Je zet de vis weer terug op de zee maar opeens de vis praat tegen jou en hij zal je 1 wens vervullen, wat voor wens maakt je dan?")
	print("A. 'Dat je een huis krijgt'")
	print("B. 'Ik ga de aller rijkste worden'")
	print("C. 'Meer vissen kunnen vangen zodat ik kan het verkopen op de markt'")
	option = input(">")
	if option in answer_A:
		game_over("Good ending", "Jij krijgt een huis voor gratis en ook een baan")
	elif option in answer_B:
		game_over("Bad ending", "de vis vindt dat je te hebberig bent en hij vervult je wens niet")
	elif option in answer_C:
		option_markt()

def option_markt():
	print("Jij verkoopt de vis, en krijgt genoeg geld om een huis te kopen. Zal je meer uitbreiden of ga je meteen huis kopen? ")
	print("A. Meer uitbreiden")
	print("B. Meteen huis kopen")
	option = input(">")
	if option in answer_A:
		game_over("Good ending", "Jij bent succesvol en je hebt huis en werk")
	elif option in answer_B:
		rupee2 = int(rupee[0])
		if rupee2 > 200:
			rupee -= 200 
			game_over("Neutral ending", "Jij hebt een huis ")
		else:
			print("Sorry jij hebt geen genoeg rupee")
			option_boot_verhuurder()

option_work_buiten_gerudotown()