#!/usr/bin/python3
import pyexcel 
def get_ip_data():
    input_ip = input('\n what is the ip add? ')
    input_driver = input('what is the driver associated with this device?')
    d = {'IP':input_ip , 'driver':input_driver}
    return d

mylistdict = []

print('Hello! This program will make you a *.xls file')

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input('\n would you like to add a another value enter \'q\' to quit')
    if (keep_going.lower()=='q'):
        break

filename = input('\n what is the name of xls file?')

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')
print('the file ' + filename + '.xls should be in your loacl directory')
    
