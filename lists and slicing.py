# #1
# ls = []
# n = int(input("Enter number: "))
# for i in range(n):
#     ele = int(input("Enter element: "))
#     ls.append(ele)
# print(min(ls))

# #2
# ls = []
# n = int(input("Enter number: "))
# for i in range(n):
#     ele = int(input("Enter element: "))
#     if ele % 2 != 0:
#         ls.append(ele)
# print(len(ls))


# #3
# def remove_element(arr, index):
#     if index < 0 or index >= len(arr):
#         return arr
#     else:
#         return arr[:index] + arr[index + 1:]
# ls = []
# n = int(input("Enter number: "))
# for i in range(n):
#     ele = int(input("Enter element: "))
#     ls.append(ele)
# print(ls)
# index = int(input("Enter index: "))
# result_array = remove_element(ls, index)
# print(result_array)


# #4
# ls = []
# n = int(input("Enter number: "))
# for i in range(n):
#     ele = int(input("Enter element: "))
#     ls.append(ele)
# minimum = min(ls)
# maximum = max(ls)
# sum_of_elements = minimum + maximum
# print(sum_of_elements)


# #5
# ls_even = []
# ls_odd = []
# n = int(input("Enter number: "))
# for i in range(n):
#     ele = int(input("Enter element: "))
#     if ele % 2 != 0:
#         ls_odd.append(ele)
#     else:
#         ls_even.append(ele)
# ls = ls_even + ls_odd
# print(ls)

# #6
# def odd_values(input_list):
#     return [input_list[i] for i in range(1, len(input_list), 2)]
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = odd_values(mylist)
# print(result)


# #7
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mylist.reverse()
# print(mylist[1:6:2])


# #8
# N = 4
# matrix = [[i + j for i in range(N)] for j in range(1, N + 1)]
# print("Matrix:")
# for row in matrix:
#     print(row)
# first_column = [row[0] for row in matrix]
# third_column = [row[2] for row in matrix]
# print("\nFirst Column:")
# print(first_column)
# print("\nThird Column:")
# print(third_column)
