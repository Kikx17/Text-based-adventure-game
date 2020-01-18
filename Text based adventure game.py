#Peli

import random
import time
a = 0

def Points():
	a+1

def displayIntro(): #Funktio 1
	print("Peli\n")
	print("Kuljet synkällä tiellä, tulet risteykseen.\n\n")

def choosePath(): #Funktio 2
	path = "" # Tämä on tyhjä, koska käyttäjä antaa sisällön myöhemmin 
	while path != "1" and path != "2": #input validation. Käytetään stringiä, koska intin käyttäminen tuottaisi ongelmia, jos käyttäjä antaa stringin vastaukseks.
		path = input("Kumpaan suuntaan käännyt? Oikealle (1) vai vasemmalle (2)? Valitse joko 1 tai 2: \n") #Kysytään käyttäjältä inputtia ja sit otetaan se talteen.

	return path

def checkPath(chosenPath): #Funktio 3
	print("Menet valitsemaasi suuntaan.")
	time.sleep(2) #Ohjelma nukkuu pari sekunttia
	print("Eteesi ilmestyy kana\n")
	time.sleep()

	correctPath = random.randint(1, 2)

	if chosenPath == str(correctPath):
		print("Annat sen jatkaa matkaansa.\n")
		Points() #Käytetään funktio Points

def pathPart2(): #Funktio 4
	omena = input("Löydät omenapuun, syötkö siitä omenan? Kyllä (1) vai ei (2)?\n").lower().strip() # stripataan user input kaikesta turhasta

	if omena.lower().strip() == "1":

		Points() #Käytetään funktio Points, lisätään pisteitä yhdellä siis
		omena = input("Juotko myös vettä? Kyllä (1) vai ei(2)?\n")
		
		if omena == "1":
			Points() #Lisätään pisteitä yhdellä
			omena = input("Jatkatko matkaa? Kyllä (1)\n")
			
			if omena == "1":
				print("Jatkat matkaa.")

			else:
				print("Peli päättyi.")
		
		elif omena == "2":
			print("Kuolit janoon. Peli päättyi.")
	
	elif omena == "2":
		print("Kuolit nälkään. Peli päättyi.")
		print("Sait pisteitä: "(a)) #Printataan pisteet


displayIntro() # Tässä käytetään kaikki funktiot
choosePath()
pathPart2()
print(a)