#!/usr/bin/python3

list1 = ['cisco_nxos','arista_eos','cisco_iso']
print (list1)
print (list1[1])
list1.extend(['juniper'])
print (list1)
list1.append(['10.1.0.1','10.2.0.1','10.3.0.1']) #append list to a list
print (list1)
print (list1[4]) #print item5
print (list1[4][0]) # print item1 within item5, we know item5 is a list

