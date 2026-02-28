#operators 
#assignment operators
a = 20
b = 28
b += a
c = 0
c += a
print(c)
print(b)

#comparision operators
a = 10
b = 20
print(a > b)
print(a == b)

#logical operators
a = 20
b = 22
print( a < b and a < b)
print( a < b or a < b)

#logical operators
a = int(input("enter a num:"))
b = int(input("enter a num:"))
print (a & b > 10 )
print(a | b < 5)
print( not a > b)

#comparison 
age = int(input("enter your age:"))
if age >=18:
    print("You are an adult")
if age < 18:
    print("you are a minor")

#Membership operators
a = input("enter a name:")
print("s" in a)
print("s" not in a)

