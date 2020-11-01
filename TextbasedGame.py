def verhaal():

    introductie = ("Hello you!\nWhat is your name?")
    naam = input()



#-------------------------------------------------------------------------------
def einde4():
    print("Two years have passed, and I've got my master's degree and I would like to stay in the Netherlands and work here.\nI have had a nice time so far with all the friends I made, and I will continue making new friends and having a good time\n, so this is my story so far.\nThis is ending 4(best ending) thank you for reading\nI hope you enjoyed it!")
    verhaal()
    einde4()
#-------------------------------------------------------------------------------
def einde3():
    print("I've made new friends and I have had a lot of fun, but after I got my master's degree i went back to work in Saudi Arabia\nThis is ending 3(neutral ending) I hope you enjoyed it!")
    verhaal()
    einde3()

#-------------------------------------------------------------------------------
def einde2():
    print("I didn't find a job so I couldn't affort an appartment or my study, so I had to go back to Saudi Arabia and went to work as a nurse there\nThis is ending 2")
    verhaal()
    einde2()
#-------------------------------------------------------------------------------
def einde1():
    print("I now work in Saudi arbia as a nurse and i didn't continue studying for my masters degree in the Netherlands.\nThis is ending 1")
    verhaal()
    einde1()
#-------------------------------------------------------------------------------
def question12a():
    print("We have had a lot of fun, but in a few weeks its finaly time to start my programm, so i should focus on that now....\nA. I can't wait\nB. Its time already?!!!")
    answer12 = input()
    if answer12 == "A" or answer12 == "a" or answer12 == "B" or answer12 == "b":
        einde4()
    else:
        print("You can only choose between choices A and B")
    question12a()
#-------------------------------------------------------------------------------
def question11a():
    print("So a few moths have passed and I invited Tatum to hang out with my new friend and I.\nWe need to decide what we should do.\nA. Go to the cinema\nB. Go to the beach")
    answer11 = input()
    if answer11 == "A" or answer11 == "a" or answer11 == "B" or answer11 == "b":
        question12a()
    else:
        print("You can only choose between the choices A or B")
    question11a()
#-------------------------------------------------------------------------------
def question10a():
    print("I don't feel comfortable making friends yet, because I'm not confident with my dutch pronunciation")
    question10a()
#-------------------------------------------------------------------------------
def question9a():
    print("I made new friends with the new language I've learned even though my pronunciation is not perfect yet.\nShould I ask Tatum to hang out with my new friend and I?\nA. Yes\nB. No")
    answer9 = input()
    if answer9 == "A" or answer9 == "a":
        question11a()
    elif answer9 == "B" or answer9 == "b":
        einde3()
    else:
        print("You can only choose between choices A or B")
    question9a()
#-------------------------------------------------------------------------------
def question8a():
    print("So I went to sign myself up for a dutch class and Tatum helped me sign up for the class\nNow I have the opportunity to make new friends in the dutch class\nSo should I make new friends there?\nA. Yes\nB. No")
    answer8 = input()
    if answer8 == "A" or answer8 == "a":
        question9a()
    elif answer8 == "B" or answer8 == "b":
        question10a()
    else:
        print("You can only choose between the choices A or B")
    question8a()
#-------------------------------------------------------------------------------
def question7a():
    print("So Tatum offered to help me with understanding dutch\n, and that is why we're calling a lot because she is teaching me dutch through discord.\nShe also told a few thing about the Netherlands and its traditions like sinterklaas and koningsdag\nWith the things that I have learned from her I can now communicate with other people.\nThat means now I can start trying to make more new friends.\nSo should i try to make new friends here?\nA. Yes\nB. No")
    answer7 = input()
    if answer7 == "A" or answer7 == "a":
        question9a()
    elif answer7 == "B" or answer7 == "b":
        question10a()
    else:
        print("You can only choose between choices A or B")
        question7a()
#-------------------------------------------------------------------------------
def question6c():
    print("I have just applied and I have been accepted to a hospital, and the good thing is the hospital is in Rotterdam, so I can go to my work when I'm done with school.\nMy programm starts in six months, so now I should try to learn dutch to make it easier to communicate with other people.\nSo I contacted my friend Tatum and asked for her help, and she gave me two choices so what should I do?\nA. Let her help me\nB. follow a course")
    answer6c = input()
    if answer6c == "A" or answer6 == "a":
        question7a()
    elif answer6c == "B" or answer6 == "b":
        question8a()
    else:
        print("You can only choose between A or B")
    question6b()
#-------------------------------------------------------------------------------
def question6b():
    print("So now i have to decide what medical unit I will apply to\nShould I apply to\nA. Intensive care unit\nB. Renal dialysis unit")
    answer6b = input()
    if answer6b == "A" or answer6b == "a" or answer6b == "B" or answer6b == "b":
        question6c()
    else:
        print("You can only choose between A or B")
    question6b()
#-------------------------------------------------------------------------------
def question6a():
    print("So I went to look for a hospital and I need to if I'm gonna work partime or fulltime.\nA. fulltime job\nB. parttime job")
    answer6a = input()
    if answer6a == "A" or answer6a == "a" or answer6a == "B" or answer6a == "b":
        question6b()
    else:
        print("You can only choose between A or B")
        question6a()
#-------------------------------------------------------------------------------

def question5a():
    print("So I found an appartment outside of Rotterdam that is less expensive, and I really should look for a job to manage to pay for it.\nI already have my bachelor degree in medical surgical nursing, so it will be easy to find a job in a hospital.\nShould I apply to a hospital?\nA. Yes\nB No")
    answer5 = input()
    if answer5 == "A" or answer5 == "a":
        quetsion6a()
    elif answer5 == "B" or answer5 == "b":
        einde2()
    else:
        print("You can only choose between A or B")
        question5a()
#-------------------------------------------------------------------------------
def question4a():
    print("So I found an appartment in Rotterdam that is very expensive, and i really should look for a job to manage to pay for it.\nI already have my bachelor degree in medical surgical nursing, so it will be easy to find a job in a hospital.\nShould I apply to a hospital?\nA.Yes\nB. No")
    answer4 = input()
    if answer4 == "A" or answer4 == "a":
        question6a()
    elif answer4 == "B" or answer4 == "b":
        einde2()
    else:
        print("You can only choose between A or B")
        question4a()
#-------------------------------------------------------------------------------
def question3a():
    print("My friend was very happy I said that i wanted to stay with him, but he said i should find a job so I went looking for one.\nI already have my bachelor degree in medical surgical nursing, so it will be easy to find a job in a hospital.\nShould I apply to a hospital?\nA.Yes\nB. No")
    answer3 = input()
    if answer3 == "A" or answer3 == "a":
        question6b()
    elif answer3 == "B" or answer3 == "b":
        einde2()
    else:
        print("You can only choose between A or B")
        question3a()
#-------------------------------------------------------------------------------
def question2a():
    print("Then my friend and I went to look for an appartment in Rotterdam where the school is. And we found 2 suitable appartments\nOne that was in Rotterdam but very expensive and the other one was outside of the city and less expensive\nWhat should I do?\nA. Take the expensive one\nB. Take the less expensive one")
    print("")
    answer2 = input()
    if answer2 == "A" or answer2 == "a":
        print("I went to look and found an expensive appartment")
        question4a()
    elif answer2 == "B" or answer == "b":
        print("I went to look for a less expensive appartment")
        question5a()
    else:
        print("you can only choose between the choices A, B or C")
        question2a()
#-------------------------------------------------------------------------------
def question1():
    print("")
    print("I found the perfect master's degree programm that you can have there. And I already booked a ticket to go to the Netherlands to arrive in Amsterdam. So I went there and when I arrived a friend of mine was waiting at the airport.\nSo we went to my friends house and I could stay there for a few days.")
    print("So I did because school hasn't started yet, and that is why a had more time to find my own appartment.\nwhat should I do because my suggested a few things.\nMy friend suggested that I should\nA. Rent an appartment\nB. Stay with him")
    answer = input()
    if answer == "A" or answer  == "a":
        question2a()
    elif answer == "B" or answer == "b":
        question3a()
    else:
        print("You can only choose between A or B")
        question1()
#-------------------------------------------------------------------------------
def introductie():
    print("Hello my name is Fahad and i'm 20 years old. I have 3 older sisters and 1 younger sisters and 1 older brother. I live or lived in Saudi Arabia,\nI study medical surgical nursing so i finished my study here and I wanted to study more in the Netherlands\n, because I found a school there so that I can continue my study")
    print("From here on the story will start.")
    print("Should i go to the Netherlands to study?\nA. Yes\nB No")
    intro = input()
    if intro == "A" or intro == "a":
        question1()
    elif intro == "B" or intro == "b":
        einde1()
#-------------------------------------------------------------------------------
def antwoord1():
    print(introductie)
    print(naam)
    print("Welcome " + naam + "Do you want to read the story of Fahad who is new in the Netherlands?\nA. Yes\nB. No")
    antw = input()
    if antw == "A" or antw == "a":
        print("Nice that you want to read the story!\nBe carefull the choices that you make can eefect the ending.\nHere is a short introduction:")
        introductie()
    elif antw == "B" or antw == "b":
        print("Maybe you have interest later!")
        verhaal()
    else:
        print("You can only choose between A or B")
    antwoord1()


verhaal()
