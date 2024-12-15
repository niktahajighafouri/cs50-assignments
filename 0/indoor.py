import sys


if len(sys.argv) > 1:
    input_string = " ".join(sys.argv[1:])
else:
    input_string = input("Enter a string: ")


print(input_string.lower())
