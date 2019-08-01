#!/usr/bin/python3
import time

def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print ('\nhandshking ... ... connecting with ' + coffeetime)
        for mycmds in devicecmd[coffeetime]:\
                print ('attempting to send my commands --->> ' + mycmds)

def main():
    work2do = {'10.1.0.1':['interface eth1/2','no shut'],'10.2.0.1':['interface eth1/1','shutdown']}
    print ('welcome to the network device command pusher')
    print ('\n data set not found')
    commandpush(work2do)

def devicereboot(IP):
    for devices in IP:
        print ('connecting to ...' + devices)
        time.sleep(1)
        print ('.')
        time.sleep(3)
        print ('connected ... rebooting....' + devices)
        time.sleep(2)
        print('reboot completed for ' + devices)

IP = ['10.1.0.1' , '10.2.0.1']

main()
devicereboot(IP)
