#ordered, unchangeable, allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
#using tuple method to make a tuple
thistuple1 = tuple(("apple", "banana", "cherry", "apple", "cherry"))
print(thistuple1)
print("-------------------------------------------")
#access tuple
print(thistuple[1])
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print("apple" in thistuple)
print("-------------------------------------------")
#update tuple
thislist = list(thistuple)
thislist[1] = "kiwi"
thistuple = tuple(thislist)
print(thistuple)
#can remove items -> want to remove-> change tuple to list
thislist = list(thistuple)
thislist.remove("apple")
thistuple = tuple(thislist)
print(thistuple)
print("-------------------------------------------")
#unpack tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print("-------------------------------------------")
#loop tuple
for x in fruits:
    print(x)





