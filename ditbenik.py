intro = "Hello you!"
print(intro.upper())
print("Ik ben Tatum")
print("wat is jouw naam?")
naam = input ()

print("")
print("wat een leuke naam, " + naam + "!")

print("")
print("Ik ben een nieuwkomer op het Mediacollege.")
print("Hier zijn en paar meer keuze vragen zodat je mij beter leert kennen.")

print("")
vraag1 = "1. Voor welke opleiding heb ik gekozen?\nA. Media developer\nB.mediavormgeving\nC. game developer:"
vraag2 = "2. Wat is mijn haarkleur?\nA. Blond\nB. Bruin\nC. rood/oranje:"
vraag3 = "3. wat is mijn hobby?\nA. Gamen\nB. Series kijken\nC. de afwas doen:"

print("")
print(vraag1)

def vraag1Juist():

    antwoordvraag1 = input()
    if antwoordvraag1 == "c" or antwoordvraag1 == "b" or antwoordvraag1 == "C" or antwoordvraag1 == "B":
        print("Klopt, dat had je goed. Eerst moet ik software developer volgen voordat ik game developer kan doen.")
    elif antwoordvraag1 == "a" or antwoordvraag1 == "A":
        print("Nee, ik heb niet voor media devoloper gekozen.")
    else:
        print("Je kan alleen maar uit de keuze a, b of c kiezen.")
        vraag1Juist()
vraag1Juist()

print("")
print(vraag2)

def vraag2Juist():

    antwoordvraag2 = input()
    if antwoordvraag2 == "c"  or antwoordvraag2 == "C":
        print("Klopt, ik heb rood/oranje haren.")
    elif antwoordvraag2 == "a" or antwoordvraag2 == "b" or antwoordvraag2 == "A" or antwoordvraag2 == "B":
        print("Nope dat is niet mijn haarkleur")
    else:
        print("Je kan alleen maar uit de keuze a, b of c kiezen.")
        vraag2Juist()
vraag2Juist()

print("")
print(vraag3)

def vraag3Juist():

    antwoordvraag3 = input()
    if antwoordvraag3 == "a" or antwoordvraag3 == "b" or antwoordvraag3 == "A" or antwoordvraag3 == "B":
        print("Klopt, ik houd van gamen en van series kijken.")
    elif antwoordvraag3 == "c" or antwoordvraag3 == "C":
         print("Wie houd er nou weer van afwassen?!")
    else:
        print("Je kan alleen maar uit de keuze a, b of c keizen.")
        vraag3Juist()
vraag3Juist()
