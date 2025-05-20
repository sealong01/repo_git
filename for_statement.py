#Python’s for statement iterates over the items of any sequence 
# (a list or a string), in the order that they appear in the sequence

#Measure strings

animals = ["dog", "cat", "horse", "goat"]

for i in animals:
    print(i, len(i))

users = {"Marlon" : "active", "Pedro" : "inactive", "Juan" : "active"}

#for user, status in users.copy().items():
#    if status == "inactive":
#        del users[user]
#print (users)

active_users = {}

for user, status in users.items():
    if status == "active":
        active_users[user] = status

print (active_users)