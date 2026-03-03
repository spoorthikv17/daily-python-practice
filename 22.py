# simple
num = int(input("enter the number:"))

if num%2==0:
    print("the no is even")
else:
    print("the no is odd")
if num%5==0:
    print("the no is divisible by 5")

##
marks = int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade C")
else:
    print("fail")

##
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>=b and a>=c:
    print("the greatest no is:",a)
elif b>=a and b>=c:
    print("the greatest no is:",b)
else:
    print("the greatest no is:",c)