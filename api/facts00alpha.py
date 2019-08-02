#!/usr/bin/python3

import requests
def main():
    '''Run this code'''
    r = requests.get('http://cat-fact.herokuapp.com/facts')
    print (dir(r))
    print (r.url)
    #print (r.json().get('all'))
    for keys in r.json().get('all'):
        pass
        #print (keys.get('text'))
main()
