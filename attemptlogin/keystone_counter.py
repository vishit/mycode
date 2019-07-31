#!/usr/bin/python3
import os
os.chdir('/home/student/mycode/attemptlogin')
file = open('keystone.common.wsgi')
x = 0
for lines in file:
    if "- - - - -] Authorization" in lines:
        print (lines)
        x = x + 1
print ('the number of failed req: ', x)
