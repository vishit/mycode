#!/usr/bin/python3

dnsfile = open('dnsservers.txt')
dnslist = dnsfile.readlines()

for srv in dnslist:
    print (srv,end=">>")
dnsfile.close()
