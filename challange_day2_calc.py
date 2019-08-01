#!/usr/bin/python3
'''this is a simple calculator'''
def main():
    '''main'''
    num1 = input("enter num1: ")
    if num1.isdigit():
        num1 = float(num1)
    else:
        print("bad input, enter intergers or floating")
        main()
    num2 = input("enter num2: ")
    if num2.isdigit():
        num2 = float(num2)
    else:
        print("bad input, enter intergers or floating")
        main()
    oper = input('enter an operator, your options are "+","-","*","/"')
    if oper == "+":
        print("Answer is ", num1+num2)
        main()
    elif oper == "-":
        print("Answer is ", num1-num2)
        main()
    elif oper == "*":
        print("Answer is ", num1*num2)
        main()
    elif oper == "/":
        if num2 == 0:
            print('cannot divide by 0, try again')
            main()
        else:
            print("Answer is ", num1/num2)
            main()
main()
