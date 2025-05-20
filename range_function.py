#function range() generates arithmetic progressions

for i in range(0,20,2):
    print(i)

# combine range and len

animals = ["dog", "cat", "horse", "goat"]

for i in range(len(animals)):
    print(i, animals[i])

d = sum(range(101))
print(d)