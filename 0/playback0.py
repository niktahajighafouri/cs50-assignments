# A program that takes user input and displays it with three dots between the words

# Get input from the user
user_input = input("Please enter your input: ")

# Add three dots between the words
output = "...".join(user_input.split())

# Display the output
print(output)