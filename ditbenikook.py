import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
decrease = '\nHelaas het is niet de goede antwoord. \n\njouw poin is vermindert 1 poin.'
Good_answer = 'Goeie Antwoord, volgende vraag'
required = ("\nAlsjeblieft gebruik A,B,C\n") #Cutting down on duplication
point = 0
#The story is broken into sections, starting with "intro"
def intro():
  print("Welkom bij de wereldgeschiedenis quiz, schrijf je naam en laten we beginnen. ")
  naam = input("Naam: ")
  print(naam +", laten we beginnen met de eerst vraag: In welk jaartal was de onafhankelijkheid van de Verenigde Staten uitgeroepen?")
  time.sleep(1)
  print ("""  A.1784 
  B. 1783
  C. 1782""")
  choice = input(">>> ") #Here is your first choice.
  global point
  if choice in answer_A:
    print(decrease)
    point -= 1
    option_president()
  elif choice in answer_B:
    print(Good_answer)
    point -= 1 
    option_president()
  elif choice in answer_C:
    print(decrease)
    point -= 1
    option_president()
  else:
    print (required)
    intro()

def option_president(): 
  print ("\nWelke generaal heeft ooit gezegd: 'Ik kom terug'?")
  time.sleep(1)
  print ("""  A. Douglas MacArthur
  B. George Patton
  C. Omar Bradley""")
  global point
  choice = input(">>> ")
  if choice in answer_A:
    print(Good_answer)
    point += 1
    option_war()
  elif choice in answer_B:
    print(decrease)
    point -= 1
    option_war()
  elif choice in answer_C:
    print(decrease)
    point -= 1
    option_war()
  else:
    print (required)
    option_war()

def option_war():
  print ("\nJij bent er bijna, Wie was de zoon van Pepijn de Korte? ")
  print ("""  A. Karel de Grote (en Carloman)
  B. Theseus
  C. Tito""")
  choice = input(">>> ")
  global point
  if choice in answer_A:
    print(Good_answer)
    point += 1 
    option_nasa()
  elif choice in answer_B:
    print(decrease)
    point -= 1
    option_nasa()
  elif choice in answer_C:
    print(decrease)
    point -= 1
    option_nasa()
  else:
     print (required)
     option_nasa()

def option_nasa():
  print ("\nHoe werd Ho Chi Minh Stad in Vietnam genoemd voor 1976? ")
  time.sleep(1)
  print ("""  A. Lutetia
  B. Shinto
  C. Saigon""")
  choice = input(">>> ")
  global point
  if choice in answer_A:
    print(decrease)
    point -= 1
    option_paus()
  elif choice in answer_B:
   print(decrease)
   point -= 1
   option_paus()
  elif choice in answer_C:
    print(Good_answer)
    point += 1
    option_paus()
  else:
    print (required)
    option_paus()

def option_paus():
  print ("\nWas Urbanus II de paus die in 1095 de gelovigen opriep om op kruistocht te vertrekken om Jeruzalem te gaan bevrijden? Y of N: ")
  time.sleep(1)
  choice = input(">>> ")
  global point
  if choice in yes:
    print(Good_answer)
    point += 1
    option_town()
  elif choice in no:
    print(decrease)
    point -= 1 
    option_town()
  else:
    print (required)
    option_town()
    
def option_town():
  print ("\nLaatste vraag: Is Parthenon gebouw in Athene die door een Venetiaanse kanonskogel in de 17e eeuw verwoest? Y of N: ")
  choice = input(">>> ")
  global point
  if choice in yes:
     print(Good_answer)
     point += 1
  elif choice in no:
    print(decrease)
    point -= 1
  else: 
    print(required)
    option_town()

def score():
  global point
  print("Your point is " + (str(point)))
  print("Thanks for playing")
  quit()

intro()
score()
