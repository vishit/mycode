#!/usr/bin/python3

round = 0
while(True):
    round = round + 1
    print ('finish the movie title "Monty Python\'s The life of ____"')
    answer = input()
    if answer.lower() == "brian":
        print ("correct")
        break
    elif answer.lower() == "shrubbery":
        print ('that my friend is the super secret answer')
        break
    elif(round == 3):
        print ('Sorry, the answer was Brian')
        break
    else:
        print('sorry try again')

