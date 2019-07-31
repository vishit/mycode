#!/usr/bin/python3
import sys

calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != 'q'): #i fixed this
    print ("\nWhat is the 1st operator? ir enter q to quit")
    calc1 = input() #i fixed it
    if calc1.lower() == 'q': #i fixed it
        break
    try:
        calc1 = float(calc1)
    except:
        print("either enter a floating point or q/Q")
        sys.exit()
    print('\nWhat is the 2nd operator? ir enter q to quit')
    calc2 = input() #i fixed it
    if calc2 == 'q':
        break
    try:
        calc2 = float(calc2)
    except:
        print("either enter a floating point or q/Q")
        sys.exit()
    print ('enter an operation to perform on the two operators (+ or -): ')
    operation = input() #i fixed it
    if operation == "+":
        print ('\n' + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2)) #i fixed it
    elif operation == "-": #i fixed it
        print ('\n' + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2)) #i fixed it
    else:
        print ("\nNot a valid entry..... restarting....")

