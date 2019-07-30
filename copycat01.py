#!/usr/bin/python3
import shutil
import os

def main():
    os.chdir("/home/student/mycode")
    shutil.copy('5g_research/ansible.txt', '5g_research/ansible.txt.copy')
    shutil.copytree('5g_research/', '5g_research_backup/')
main()

