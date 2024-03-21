# #1
# num = int(input("Enter number: "))
# ls = [i for i in range(1, num+1)  if i % 2 == 0]
# print(sum(ls))


# #2
# ls = [i for i in range(1, 201) if i % 2 == 0]
# print(ls)


# #3
# n = int(input("Enter number: "))
# ls = [(a, b, int((a**2 + b**2) ** 0.5)) for a in range(1, n+1) for b in range(a, n+1) if ((a**2 + b**2) ** 0.5).is_integer() and (a**2 + b**2) ** 0.5 <= n]
# print(ls)


# #4
# ls = [3, 4, 5, 6]
# length = 4
# result = [[ls + i for i in range(length)] for ls in ls]
# print(result)
