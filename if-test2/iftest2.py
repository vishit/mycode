#!/usr/bin/python3

def main():
    ipchk = input("enter ip add: ")
    if ipchk == '192.168.1.70':
        print ("cannot set to gw ip")
    elif ipchk:
        print ('looks like the ip add was set: ' + ipchk)
    else:
        print("no data rx")
main()
