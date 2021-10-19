#unordered, unchangeable, duplicates not allowed
thisset = {"apple", "banana","cherry", "apple"}
print(thisset)
print(len(thisset))
#using set method
thisset = set(("apple","banana","cherry"))
print(thisset)
print("------------------------------------")
#access set
for x in thisset:
    print(x)
print("apple" in thisset)
print("------------------------------------")
#add set -> unchangeable but can add
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print("------------------------------------")
#remove : using remove or discard
thisset.discard("apple")
print(thisset)
thisset.pop() #remove last item
print(thisset)
print("------------------------------------")
#loop set
for x in thisset:
    print(x)
print("------------------------------------")
#join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1.update(set2)#insert items in set2 into set1
print(set1)



