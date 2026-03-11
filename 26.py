keep_running = True
while keep_running:
    user_input = input("Type 'exit' to stop: ").lower()
if user_input == 'exit':
    keep_running = False
else:
    print("You typed:", user_input)
 
print("Loop has ended.")
