# A program that takes user input and displays it with three dots between the words

def convert(input_text):
    """
    Converts emoticons in the input text to corresponding emojis.
    :param input_text: str
    :return: str
    """
    return input_text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    # Get input from the user
    user_input = input("Please enter your text: ")

    # Call the convert function and display the output
    output = convert(user_input)
    print(output)


if __name__ == "__main__":
    main()
