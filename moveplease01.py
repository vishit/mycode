#!/usr/bin/python3
import shutil
import os

def main():
    os.chdir("/home/student/mycode")
    shutil.move('raynor.obj', 'ceph_storage/') #move file
    xname = input('enter new file name for kerrigan.obj') 
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/'+ xname) #rename file
main()
