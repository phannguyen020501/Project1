def my_function():
    print("hello from a function")

my_function()
print("------------------------------")
def my_function1(fname):
    print(fname + "Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")
print("------------------------------")
def my_function2(fname, lname):
    print(fname + " " + lname)
my_function2("Emil", "Refsnes")
print("------------------------------")
#if dont know how many arguments, add * before parameter name in the function
def my_function3(*kids):
    print("The youngest child is "+kids[2])

my_function3("Emil","Tobias","Linus")
print("------------------------------")
#keyword arguments
def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)

my_function4(child1="Emil", child2="Tobias", child3="Linus")
print("------------------------------")
#**
def my_function5(**kid):
    print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname="Refsnes")
print("------------------------------")
#default parameter value:
def my_function6(country = "Norway"):
    print("I am from " + country)

my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")
print("------------------------------")
#passing a list as an argument
def my_function7(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function7(fruits)
print("------------------------------")
#return values
def my_function8(x):
    return 5*x
print(my_function8(3))
print(my_function8(5))
print("------------------------------")
#recuision
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n Recursion example results")
tri_recursion(6)
print("------------------------------")


