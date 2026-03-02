##simple dict
menu ={
    "pizza": 120,
    "burger": 80,
    "juice": 40
}
item = input("Enter the item:")
if item in menu:
    print("Price:",menu[item])
else:
    print("item not found")

##
print(menu.keys())
print(menu.values())
print(menu.items())

p = {
    "class": "12th",
    "sec": "A",
    "roll":23
}
menu.update(p)
print(menu)