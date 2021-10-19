i = 1
while i < 6:
    print(i)
    i+=1
print("----------------------")
#break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1
print("----------------------")
#continue
i = 1
while i < 6:
    i+=1
    if i == 3:
        continue
    print(i)
print("----------------------")
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)
for x in range(2, 30, 3):
    print(x)
