# Fibonnaci

# class New:

#     def fib(num, a, b):
#         # a, b = 0, 1
#         print("Fibonacci Series:", a, b, end = " ")
#         for i in range(2, num):
#             n = a + b
#             a = b
#             b = n
#             print(n, end = " ")

#         print()

# k = New
# k.fib(10, 0, 1)



num = 10
a, b = 0, 1
print("Fibonacci Series:", a, b, end=" ")
for i in range(2, num):
    n = a + b
    a = b
    b = n
    print(n, end=" ")
# print()