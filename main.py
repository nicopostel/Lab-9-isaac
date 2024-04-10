#isaac philipose

def encoder(data):
    pass



def decoder(data):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = int(input("Please enter your password to encode: "))
            encode = encoder(password)
        if choice == 2:
            decode = decoder(encode)
            print(f"The encoded password is {encode}, and the original password is {decode}")
        if choice == 3:
            break

if __name__ == "__main__":


