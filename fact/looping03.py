#!/usr/bin/python3
import uuid

howmany = int(input("how many uuids muct be generated?"))

print ("generating uuids")

for rando in range(howmany):
    print(uuid.uuid4())

