class greatest:
    def solution(self):
        a = input("input for a:")
        b = input("input for b:")

        if a > b:
            print("A is greater")
        else:
            print("b is greater")



class derived(greatest):
    access = greatest()
    access.solution()