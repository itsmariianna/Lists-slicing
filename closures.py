# #1. Counter Function: Create a closure that captures a counter variable initialized to 0. The closure should allow incrementing and returning the counter value each time it is called.
# def counter_function():
#     count = 0
#     def incrementing_function():
#         nonlocal count
#         count = count + 1
#         return count
#     return incrementing_function
# new_function = counter_function()
# print(new_function())
# print(new_function())
# print(new_function())



# #2. Accumulator Function: Write a closure that behaves as an accumulator. The outer function should accept an initial number, and the inner function should accept a number to add to the accumulator, returning the new total each time it is called.
# def accumulator_function(x):
#     count = x
#     def inner_function(y):
#         nonlocal count
#         count = count + y
#         return count
#     return inner_function
# foo = accumulator_function(0)
# print(foo(10))
# print(foo(4))
# print(foo(60))



# #3. Tag Generator: Develop a closure for generating HTML tags. The outer function should take the tag type (e.g., ‘p’, ‘div’), and the inner function should take content to wrap with the specified tag.
# def outer(tag):
#     def inner(content):
#         return f'<{tag}>{content}</{tag}>'
#     return inner
# x = outer("div")
# print(x("email-content"))



# #4. Exponentiation Function: Implement a closure that allows you to create functions for different powers. For example, a general function power_of(x) that returns another function for a specific power, such as square = power_of(2) where square(3) should return 9 (3 squared).
# def power_of(e):
#     def raise_power(x):
#         return x ** e
#     return raise_power
# square_of = power_of(2)
# print(square_of(5))
# cube_of = power_of(3)
# print(cube_of(7))




#5. Memoization Function: Write a closure that implements memoization for a given function. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again.
#chem haskacel




# #6. Function Call Counter: Make a closure that wraps any function and counts how many times that function has been called, returning the count along with the function’s result each time.
# def call_counter(foo):
#     count = 0
#     def wrapper(*args):
#         nonlocal count
#         count = count + 1
#         result = foo(*args)
#         return count, result
#     return wrapper
# def func(a, b):
#     return a * b
# result = call_counter(func)
# print(result(13, 56))
# print(result(43, 90))
# print(result(15, 6))



#7. Access Control: Create a closure that provides a simple access control layer. The outer function should accept an authorized user ID, and the inner function should only execute its logic if the correct user ID is provided, otherwise, it should return “Unauthorized”.
#chem haskacel




# #8. Limit Call Function: Design a closure that limits the number of times a function can be called. After the function has been called a specified number of times, any further attempts should return a message saying that the limit has been reached.
# def limit_function(func, limit):
#     count = 0
#     def wrapper(*args,):
#         nonlocal count
#         if count < limit:
#             count += 1
#             return func(*args)
#         else:
#             return "Your entered limit reached for this function.".format(limit)
#     return wrapper
# def greet(name):
#     return "Hello, {}!".format(name)
# result = limit_function(greet, int(input("Enter limit:")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
# print(result(input("Enter name: ")))
