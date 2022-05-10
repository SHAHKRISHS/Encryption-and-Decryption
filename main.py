from cryptography.fernet import Fernet
from termcolor import colored
from os.path import exists


# Take the text from the user.
text = input("Enter the text you want to encrypt: \n")

# Encoded the message
text_encode = text.encode()

# generate the key.
key = Fernet.generate_key()

# Encrypt the encoded text.
f = Fernet(key)
encrypted = f.encrypt(text_encode)

# To give choice to select either they want to decrypt or not

choice = input("Do you want to Decrypt the text ( Y or N ): ")
choice = choice.upper() # For converting the character into uppercase.

if choice == 'Y':
    print("\nThe original Text is: ", colored(text, "green"))
    print("The Encrypted Text is: ", colored(encrypted.decode(), "green"))
    # Decrypt the text
    f1 = Fernet(key)
    decrypt = f1.decrypt(encrypted)

    # Decoded the message
    text_decode = decrypt.decode()
    print("The decrypted text is:", colored(text_decode, "green"))
    result = input("Do you want to save the result into a text file ( Y or N ): ")
    result = result.upper()

    if result == 'Y':
        file_name = input("Enter the name of the file: ")
        file_name = file_name+".txt"
        file_exists = str(exists(file_name))
        if file_exists == "True":
            choice = int(input(
                "Please select from below options: \n 1. Append to the file. \n 2. Overwrite the file. \n Please select the option: "))

            if choice == 1:
                # Append to the file
                with open(file_name, "a") as file_open:
                    line1 = "The original Text is", text
                    line2 = "The Encrypted Text is:", encrypted.decode()
                    line3 = "The Decrypted Text is:", decrypt.decode()

                    # It will write the multiple lines in the text file
                    file_open.write("\n")
                    file_open.writelines(str([line1, line2, line3]))

                    print("The output has been saved in the file named", colored(file_name, "green"))

            if choice == 2:
                # Overwrite the file
                with open(file_name, "w") as file_open:
                    line1 = "The original Text is", text
                    line2 = "The Encrypted Text is:", encrypted.decode()
                    line3 = "The Decrypted Text is:", decrypt.decode()

                    # It will write the multiple lines in the text file
                    file_open.writelines(str([line1, line2, line3]))
                    print("The output has been saved in the file named", colored(file_name, "green"))

        else:
            file = open(file_name, "x") # Create a text file
            # Writes in a text file
            with open(file_name, "w") as file_open:
                line1 = "The original Text is", text
                line2 = "The Encrypted Text is:", encrypted.decode()
                line3 = "The Decrypted Text is:", decrypt.decode()

                # It will write the multiple lines in the text file
                file_open.writelines(str([line1, line2, line3]))
                print("The output has been saved in the file named", colored(file_name, "green"))

else:
    print("The original Text is:", colored(text, "green"))
    print("The Encrypted Text is:", colored(encrypted.decode(), "green"))

    # To save the result in the text file
    result = input("Do you want to save the result into a text file ( Y or N ): ")
    result = result.upper()

    if result == 'Y':
        file_name = input("Enter the name of the file: ")
        file_name = file_name + ".txt"
        file_exists = str(exists(file_name))
        if file_exists == "True":
            choice = int(input("Please select from below options: \n 1. Append to the file. \n 2. Overwrite the file. \n Please select the option: "))

            if choice == 1:
                with open(file_name, "a") as file_open:
                    line1 = "The original Text is", text
                    line2 = "The Encrypted Text is:", encrypted.decode()

                    # It will write the multiple lines in the text file
                    file_open.write("\n")
                    file_open.writelines(str([line1, line2]))
                    print("The output has been saved in the file named", colored(file_name, "green"))

            if choice == 2:
                with open(file_name, "w") as file_open:
                    line1 = "The original Text is", text
                    line2 = "The Encrypted Text is:", encrypted.decode()

                    # It will write the multiple lines in the text file
                    file_open.writelines(str([line1, line2]))
                    print("The output has been saved in the file named", colored(file_name, "green"))

        else:
            file = open(file_name, "x") # Create a text file
            # Writes in a text file
            with open(file_name, "w") as file_open:
                line1 = "The original Text is", text
                line2 = "The Encrypted Text is:", encrypted.decode()

                # It will write the multiple lines in the text file
                file_open.writelines(str([line1, line2]))
                print("The output has been saved in the file named", colored(file_name, "green"))