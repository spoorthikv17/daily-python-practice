##while loop
i = 1
while i<=9:
    print(f"{i}")
    i+=1

##
count = 1
while count <=10:
    print(f"{count}")
    if count == 8:
        print("thats enough!!")
        break
    count+=1

##
sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 2:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1

