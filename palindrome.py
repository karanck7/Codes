

class Pal:
    
    def __init__(self):
        a = str(input("Enter a string:" ))

        if a == a[::-1]:
            print("The string is a Palindrome")
        else:
            print("The string is not a palindrome")

b = Pal()
b.__init__()

