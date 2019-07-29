#!/usr/bin/python3
my_list = ['192.168.0.5',5060,"UP"]
print ("the first item in the list (IP): " + my_list[0])

print ("the 2nd item is a port: " + str(my_list[1]))

print ("the third item is status " + my_list[2])

new_list = [5060 , "80", 55 , "10.0.0.1", '10.20.30.1', "ssh"]

print ("When i ssh into IP add ",new_list[3],"or ",new_list[4],"I am able to ping ports",new_list[0], new_list[1], "or", new_list[2])
