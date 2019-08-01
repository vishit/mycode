#!/usr/bin/python3

from subprocess import call

call (['ip','link','show','up'])

print ('this program will check your interface')

interface = input('enter an interface like ens3: ')

call (['ip','addr','show','dev',interface])

call (['ip','route','show','dev',interface])

