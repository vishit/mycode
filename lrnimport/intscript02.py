#!/usr/bin/python3

import subprocess

subprocess.call (['ip','link','show','up'])

print ('this program will check your interface')

interface = input('enter an interface like ens3: ')

subprocess.call (['ip','addr','show','dev',interface])

subprocess.call (['ip','route','show','dev',interface])

