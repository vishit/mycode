#!/usr/bin/python3
configfile = open ('vlanconfig.cfg', 'r')

print (configfile.read())

configfile.close()

configfile = open ('vlanconfig.cfg', 'r')
configlist = configfile.readlines()

print (configlist)

for x in configlist:
    print (x.strip("\t"), end= "")

configfile.close()

