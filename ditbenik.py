import datetime 
import time
import requests
from AnilistPython import Anilist
anilist = Anilist()
import itertools
import random 

questions = ["Waar woon ik?",
             "Met wie woon ik?",
             "Van welke land kom ik?",
             "Wie is mijn waifu?"]

answers = ["a)Haarlem\nb)Enkhuizen\nc)IJmuiden\nd)Utrecht\n-->",
           "a)Moeder\nb)Moeder + Vader\nc)Vader\nd)Oom\n-->",
           "a)Japan\nb)Malaise\nc)Indonesie\nd)Singapore\n-->",
           "a)Rikka Takanashi\nb)Mai Sakurajima\nc)Nezuko Kamado\nd)Marin Kitagawa\n-->"
            ]

correct_choices = ["c","a","c","b"]

options = ["a","b","c","d"]

correct_answer = ["IJmuiden",
           "Moeder",
           "Indonesie",
           "Mai Sakurajima"]

scores = {}

def anime():
	print("Do you like Anime? What's your favourite character?")
	AnimeChar = input("Name Character: ")
	time.sleep(3)
	try:
		anilist.print_character_info(AnimeChar)
	except:
		raise IndexError('Sorry, it seems I can not find your character. Please restart the program manually.')
	print("-----------------------")

def quiz(questions, answers, correct_choices): 
    score = 0 
    wrong_answers = []

    for question, answer, correct_choices in zip(questions, answers, correct_choices):
        print(question)
        print("=================")
        print("[Please choose a,b,c,d]")
        print("=================")
        user_answer = input(answer).lower()               
        while user_answer not in options:
            print("please select only on of the given options.eg:a,b,c,d")
            user_answer = input(answer).lower()
        else:
            if user_answer in correct_choices:
            	score += 1   
            	print("Good Answer, next question")        
            else:
                print("Wrong Answer, next question")          
    print("Great Work","You've finished the game!")    
    print("****Your Score****")
    print(score, "out of", len(questions), "correct answers")
 
def the_bot(): 
	print("In which year do you born?")
	time.sleep(2)
	Birthyear = int(input("Birth Year: "))
	currentDate = datetime.datetime.today().date()
	age = currentDate.year - Birthyear
	print("It is now " + str(currentDate.year)) 
	print("So your age is now " + str(age))

	print("Loading more Specific Age Calculator........")
	time.sleep(5)

	date = datetime.datetime.today()
	print("The date of today is: " + str(date))
	print("What's your birthday?")
	time.sleep(2)
	AgeBirth = input("BirthDay with the order Day/Month/Year in numbers: " )
	AgeBirth = datetime.datetime.strptime(AgeBirth, "%d/%m/%Y").date()
	print("Your birthday is on "+ AgeBirth.strftime("%d") + " of " + AgeBirth.strftime("%B, %Y"))
	currentDate = datetime.datetime.today().date()
	age2 = currentDate.year - AgeBirth.year
	month = currentDate.month - AgeBirth.month
	date = currentDate.day - AgeBirth.day
	age2 = int(age2)

	if month < 0 :
		age2 = age2-1
	elif date < 0 and month == 0:
		age2 = age2-1

	time.sleep(5)
	print("Your age is {0:d}".format(age2))
	anime()
    


def the_bot2():
	print("Hallo!, I'm Bot. What's your name?")
	time.sleep(2)
	Name = input("Name: ")
	print("Hallo " + Name)
	print("In which year do you born?")
	time.sleep(2)
	Birthyear = int(input("Birth Year: "))
	currentDate = datetime.datetime.today().date()
	age = currentDate.year - Birthyear
	print("It is now " + str(currentDate.year)) 
	print("So your age is now " + str(age))

	print("Loading more Specific Age Calculator........")
	time.sleep(5)

	date = datetime.datetime.today()
	print("The date of today is: " + str(date))
	print("What's your birthday?")
	time.sleep(2)
	AgeBirth = input("BirthDay with the order Day/Month/Year in numbers: " )
	AgeBirth = datetime.datetime.strptime(AgeBirth, "%d/%m/%Y").date()
	print("Your birthday is on "+ AgeBirth.strftime("%d") + " of " + AgeBirth.strftime("%B, %Y"))
	currentDate = datetime.datetime.today().date()
	age2 = currentDate.year - AgeBirth.year
	month = currentDate.month - AgeBirth.month
	date = currentDate.day - AgeBirth.day
	age2 = int(age2)

	if month < 0 :
		age2 = age2-1
	elif date < 0 and month == 0:
		age2 = age2-1

	time.sleep(5)
	print("Your age is {0:d}".format(age2))
	anime()
	quit()


print("Hallo!, I'm Bot. What's your name?")
time.sleep(2)
Name = input("Name: ")
print("Hallo " + Name)
print("I am a newcomer to the Mediacollege Amsterdam. To get to know me better, I ask a few questions about me.")
time.sleep(5)
quiz(questions, answers, correct_choices)
the_bot()

def quit():
	answer = str(input(Name + " , would you like to restart the program? Y or N: "))
	if answer == 'Y':
		print("Okay, restarting the program...")
		time.sleep(5)
		the_bot2()
	elif answer == 'N': 
		print("Okay, Have a nice day...")
	else:
		print("INVALID OPTION, BREAKING THE PROGRAM AUTOMATICALLY...")
