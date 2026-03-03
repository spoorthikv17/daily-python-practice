#condition statement

age = int(input("enter your age:"))
if age < 5:
    print("The bus pass is free")
elif age>=60:
    print("Senior citizen discount")
else:
    print("pay the full price")

##simple example'
time = int(input("Enter the time :"))

if time == 8:
    print("Brekfast time")
elif time == 1:
    print("Lunch time")
elif time == 8:
    print("Dinner time")
else:
    print("It's not meal time")
