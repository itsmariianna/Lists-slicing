# # Testi 8rd xndiry
# def twosum(nums: list[int], target: int):
#     for j in range(len(nums)):
#         for i in range(len(nums)):
#             if nums[j] + nums[i] == target:
#                 return [i, j]
#     return "There are no values which sum is equal to your target"
            
# my_list = [2, 7, 11, 15]
# hit = 9
# result = twosum(my_list, hit)
# print(result)



# # Stugel tivy 4i astichan e te voch
# def four(n):
#     if (n & (n - 1) == 0) and (n % 3 == 1):
#         return "The number is exponentiation of 4"
#     else:
#         return "The number is not exponentiation of 4"
# my_num = int(input("Enter number: "))
# print(four(my_num))



# # Deep copy
# ls = [1, 2, 3, 4]
# new_ls = []
# for i in ls:
#     new_ls.append(i)
# new_ls[0] = 'hello'
# print(ls)
# print(new_ls)