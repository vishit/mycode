#!/usr/bin/python3
import csv

def main():
    f = open('csv_users.txt','r')
    i = 0
    for row in csv.reader(f):
        i = i + 1
        filename = "admin.rc%d"%i
        rcFile = open(filename, 'w')
        print ('export OS_AUTH_URL=' + row[0], file=rcFile)
        print ('export OS_IDENTITY_API_VERSION=3', file=rcFile)
        print ('export OS_PROJECT_NAME=' + row[1], file=rcFile)
        print ('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcFile)
        print ('export OS_USERNAME=' + row[3], file=rcFile)
        print ('export OS_USER_DOMAIN_NAME=' + row[4], file=rcFile)
        print ('export OS_PASSWORD=' + row[5], file=rcFile)
        print (row)
        rcFile.close()
main()

