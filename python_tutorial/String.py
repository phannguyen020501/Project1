a = "Hello, world! "
print(a[1])
print(a[2:5]) #get characters form pos 2 to 5(not included)
print(a[:5]) #get characters form the start to 5(not included)
print(a[2:]) #get characters form pos 2 to the end
print(a.upper()) #upper case
print(a.lower()) #lower case
print(a.strip()) #remove white space from the beginning or the end
print(a.replace("H","J")) #replace
print(a.split(",")) #split by ","
print(len(a))
print("--------------------------------")
#check string
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
print("--------------------------------")
#format string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity,itemno,price))
print("--------------------------------")
