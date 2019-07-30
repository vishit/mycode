#!/usr/bin/python3
switch = {'hostname':'sw1','ip':'10.0.1.1','version':'1.2', 'vendor' : 'cisco'}

print (switch['hostname'])
print (switch['ip'])

#print (switch['lynx'])

#requesting a fake key with the .get method

print ("test1 - .get()")
print (switch.get('lynx'))

print ("test2 - .get()")
print (switch.get('lynx', "the key is in another castle!"))

print ("test3 - .get()")
print (switch.get('version', 'aaha the sw verison'))

print ("test4 - .keys()")
print (switch.keys())

print ("test5 - .values()")
print (switch.values())


print ("test6 - .pop()")
switch.pop('version')
print (switch.keys())
print (switch.values())

print ("test7 - add new pair")
switch['adminlogin']='karl08'
print (switch.values())
print (switch.keys())

print ("test8 - add new pair")
switch['password']='querty'
print (switch.keys())
print (switch.values()) 
