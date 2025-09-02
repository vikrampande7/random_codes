'''Reverse a List'''
# a = [1,2,3,4,5,6,7,8,9]
# def reverse(list):
#     b = []
#     count = len(list)-1
#     for i in range(len(a)):
#         new_element = a[count]
#         b.append(new_element)
#         count -= 1
#     return b
# reverse(a)

'''Continue-Break'''
# a = [1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i == 2:
#         continue
#     if i == 7:
#         break
#     else:
#         print(i)

'''Sort List'''
# a = [6,3,7,8,5,3,8,3]
# b = [6,3,7,99,14,1,5,6]

# def sort_list(a, b):
#     c = a + b
#     d = list(set(c))
#     e = sorted(d)
#     return e

# def sort_list_one_liner(a,b):
#     return sorted(set(a+b))

# j = sort_list(a, b)
# k = sort_list_one_liner(a, b)

# if j == k:
#     print('yes')

'''List Comprehension'''
# a = [6,3,7,8,5,3,8,3]

# b = [i*2 for i in a]
# print(b)

# a = ['Vikram Pande',
# 'Atharva Pawar',
# 'Ameya Vaichalkar',
# 'Kartik Rawool',
# 'Subodh Gujar']

# def trim_lastname(alist):
#     return [i.split(' ')[-1] for i in a]

# print(trim_lastname(a))

'''MAP function'''
# x = [1,2,3,4,5,6,7,8,9]
# def make_odd(i):
#         if i%2==0:
#             return i+1
#         else:
#             return i

# y = list(map(make_odd,x))
# print(y)
