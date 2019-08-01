#!/usr/bin/python3

import subprocess
'''this program will do a ls -al in whichever directory you specify'''

USER = input('enter the directory that you wanna see: ')
def main():
    subprocess.call (['ls', '-al', USER])

main()

