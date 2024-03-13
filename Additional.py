# #Additional
#1


# #2
# def decimal_to_binary(n):
#     return bin(n)[2:]
# number = int(input("Enter number: "))
# result = decimal_to_binary(number)
# print("The result is: ", result)


# #3
# def sum_of_integers(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_of_integers(n // 10)
# number = int(input("Enter number: "))
# result = sum_of_integers(number)
# print("The sum of integers is: ", result)


# #4
# def foo(a, b):
#     if b == 0:
#         return a
#     else:
#         return foo(b, a % b)
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# result = foo(number1, number2)
# print("The greatest greatest common divisor is: ", result)


# #5
# def foo(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# result = foo(number1, number2)
# print("The greatest greatest common divisor is: ", result)


# #6
# def fibonaci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)
# number = int(input("Enter number: "))
# print("The result is ", fibonaci(number))