#eligibility check
age = int(input("enter your age:"))
if age < 18:
    print("Student membership")
elif age >=60:
    print("Senior citizen membership")
else:
    print("regular membership")

##
att = int(input("enter the att in percentage:"))

if att >75:
    print("exam")
elif att >=60 and att <=75:
    print("reexam")
elif att >=50 or att <60:
    print("no exam")
else:
    print("detained")
