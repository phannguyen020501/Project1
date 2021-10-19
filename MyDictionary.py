#store data in key: value
#changeable, duplicates not allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print("----------------------------")
#accessing items
x = thisdict.get("model")
print(x)
x = thisdict.keys()#list keys
print(x)
x = thisdict.values()#list values
print(x)
x = thisdict.items()#list key and value
print(x)
print("model" in thisdict )#check key
print("----------------------------")
#change values
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"made in": "China"})
print(thisdict)
print("----------------------------")
#adding items
thisdict["color"] = "red"
print(thisdict)
print("----------------------------")
#remove items
thisdict.pop("model")
print(thisdict)#using clear to empty dict
print("----------------------------")
#loop
for x in thisdict:
    print(x) #keys
    print(thisdict[x])#values
for x, y in thisdict.items():
    print(x,y)
print("----------------------------")
#nested, a dictionary can contain dictionaries
myfamily = {
    "child1": {
        "name": "Emy",
        "year": "2004"
    },
    "child2":{
        "name":"Alice",
        "year":"2007"
    }
}
print(myfamily)




