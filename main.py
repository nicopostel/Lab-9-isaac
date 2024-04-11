#isaac philipose

def encoder(data):
    newstrdata = ""
    for i in range(len(data)):
        convert = str(3+int(data[i]))
        if len(convert) > 1:
            convert = convert[1:]
        newstrdata+= convert

    return newstrdata





def decoder(data):
    pass

def main():
    encode = 0
    decode = 0

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encode = encoder(password)
            print("Your password has been encoded and stored!")
        if choice == 2:
            decode = decoder(encode)
            print(f"The encoded password is {encode}, and the original password is {decode}")
        if choice == 3:
            break

if __name__ == "__main__":
    main()

