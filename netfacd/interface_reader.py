#!/usr/bin/python3

import netifaces
print (netifaces.interfaces())

adapter = input('what adapter do you want info for.... your options are [lo,ens3, docker0]')
adapter_list = ['lo','ens3', 'docker0']

if adapter in adapter_list:

for i in netifaces.interfaces():
    try:
        print ('\n ****details of interfcaes -' + i + '****')
        print ('MAC: ',end='')
        print (netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])#print mac
        print ('IP: ',end='')
        print (netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])#print IPs
    except:
        print('could not collet adapter info')
if 
def IP(adapter):
    ''' to get IP for an IP'''

def MAC(adapter):
    '''to get MAC for an adapter'''
