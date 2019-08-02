#!/usr/bin/python3
#import requests
import json
import urllib.request

URL_VAR = 'http://api.open-notify.org/astros.json'

def final_answer(astro,craft):
    print (f"{astro} is on {craft}")

def main():
    groundctrl = urllib.request.urlopen(URL_VAR)
    #print (groundctrl)
    
    read_page = groundctrl.read() # read webpage
    #print(read_page)
    
    decode_data = json.loads(read_page.decode('utf-8'))
    x = int(decode_data['number'])
    print (f'Total Astro in space {x}') #find total number
    for i in range(x):
        final_answer(decode_data['people'][i]['name'], decode_data['people'][i]['craft'])

main()

