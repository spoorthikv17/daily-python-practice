##pin using while
pin ="" #initially pin is empty string
correct_pin = 2082006
while pin!=correct_pin:
    pin = int(input("enter your pin:"))
    if pin == correct_pin:
        print("crct pin")
    else:
        print("wrong pin")

##
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

    