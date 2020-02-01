import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Its necessary to put more than one object")
    else:
        if sys.argv[1] == 'help' or sys.argv[1] == "ayuda":
            print("Contact with this number 923484 have a nice day...")
        print(sys.argv[1:])
