import random
import string
import sys


def start():

    a = input("Type 'h' to learn commands ")
    if a == "q":
        sys.exit()
    elif a == "h":
        help()
    elif a == "g":
        return core()
    else:
        print("You entered invalid value, try again please :/")
        return start()

def generate(size = 0):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

        return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


def show(x):
    print(x)
    c = input("To save 's', to quit 'q', to restart 'r'")
    if c == "s":
        return save(x)
    elif c == "help":
        return help()
    elif c == "q":
        sys.exit()
    elif c == "r":
        core()
    else:
        print("Invalid input, generator will be restart!")
        return start()

def save (password2):
    purpose = str(input("Enter the purpose or direction of password :  "))
    password = open("Saved_Pass.txt","a")
    password.write(password2)
    password.write(" ----------------> ")
    password.write(purpose)
    password.write("\n")
    password.close()


def help():
    print("mainscreen commands : ", "\n" 
          " 'g' ---------------> generate the pass", "\n",
          "'q' ---------------> exit the program", "\n",
          "'r' ---------------> restart the program","\n")


    start()

def core () :

    a = int(input("How many digits you need : "))
    generated_pass = generate(a)

    option = input("Your password generated. To see 'l', to save 's', to exit 'q'")

    if option == "l":
        return show(generated_pass)
    elif option == "s":
        return save(generated_pass)
    elif option == "q":
        return sys.exit()
    else :
        print("Invalid input")
        b = input("Type 'q' for exit, 'r' for restart")
        if b == "q":
            sys.exit()
        elif b == "r":
            start()





print("-------------WELCOME TO NEBULOSUS PASS-GEN 0.1----------------")


start()