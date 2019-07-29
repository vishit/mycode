#!/usr/bin/python3
proto = ["ssh","http","https"]
protoa = ["ssh","http","https"]
print (proto)
proto.append('dns') #add dns to the list
protoa.append('dns') #add dns to the list
print (proto)
proto2 = [22,80,443,53] 

proto.extend(proto2) #same as merging the 2 lsits.


print (proto)

protoa.append(proto2) # append the entire list proto2 to the end of list protoa 
print (protoa)
