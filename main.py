"""
Lab 6
Authors: Marco Fernandez and Noah Adelson
Class: COP3502
Section: 22282
Description: This lab we will use Git in order to collaborate on a password encoder/decoder program.
"""


def main():
    initial_password = ""
    encoded_password = ""
    decoded_password = ""

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("\nPlease enter an option: ")

        if option == '1':
            initial_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(initial_password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if initial_password != "":
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {initial_password}.")

        elif option == '3':
            break


def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decode_password(encoded_password):
    decoded_password = ""
    for i in encoded_password:
        n = int(i)
        n -= 3
        if n < 0:
            n+=10
        decoded_password += str(n)
        return decoded_password


if __name__ == "__main__":
    main()
