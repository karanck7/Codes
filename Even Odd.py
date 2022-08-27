class evenOdd:

    def takeInput(self):
        x = int(input("enter a number:" ))

        if (x%2 == 0):
            print("even")
        else:
            print("odd")

y = evenOdd()
y.takeInput()
