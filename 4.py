# simple love project
print("Love")

# input function is used to take user input
Boy_name = input("boy name:")
girl_name = input("girl name: ")

# int used to convert the input string to an integer
boy_age = int(input("boy age:"))
girl_age = int(input("girl age:"))

# abs is used to get the absolute value of the age difference irrespective of signs
age_diff = abs(boy_age - girl_age)

# f string is used to foramt the output string with variables
print(f"{Boy_name} loves {girl_name}. Age difference is {age_diff}")

# concatenation method
print( Boy_name + " loves " + girl_name  + ". Age difference is" + str(age_diff))