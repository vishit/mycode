#!/usr/bin/python3

def main():
    filename = input("please input filename:> ")
    configfile = open (filename, 'r')
    configblog = configfile.read()
    configlist =configblog.splitlines()
    print (configlist)
    configfile.close()
    print(len(configlist))
main()
