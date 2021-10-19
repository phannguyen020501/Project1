#ordered, changable, allow duplicates
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#list can contain different datatypes
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print("----------------------")
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[1])
print(mylist[2:5])
print(mylist[:4])
print("----------------------")

#changelist
mylist.append("orange")
print(mylist)
mylist.remove("orange")
print(mylist)
mylist.insert(1,"orange")
print(mylist)
tropical = ["mango", "pineapple", "papaya"]
mylist.append(tropical)
print(mylist)
print("----------------------")

#loop
for x in tropical:
    print(x)

for x in range(len(tropical)):
    print(x)

[print(x) for x in tropical] #short hand

print("----------------------")
#short list
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print("after sort: ")
print(thislist)
thislist.sort(reverse= True) #sort descending
print(thislist)
print("----------------------")


