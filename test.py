# my_list1 = ['apple','banana']
# my_list2 = ['boll','cat']

# a = [i  for i in my_list1]
# b = [i  for i in my_list2]
# # print(a)

# c = zip(a,b)

# d  = list(c)

# res2 = [x for x in d]
# # print(res2)

# res = {i:j for i,j in zip(my_list1,my_list2)}

# # print(res)


# my_dict = {'career': 'TeleTalk', 'country': 'Bangladesh', 'name': 'Maateen'}



# # print(my_dict)

# new_dict = {key:value for key,value in my_dict.items()}
# # print(new_dict)


# number = int(input("Enter Your Favarite Number : "))


# temp = number

# # print(number)
# print(temp)


# while number > 1:
#     number -=1

#     # print(number)

#     temp  *= number


# # print(temp)





# my_list = [1,2,3,4,5,6]


# def square (x):
#     return x * x


# new_list  = map(square,my_list)

# print(list(new_list))


a,b,c = map(int,int(input("Enter Your Best Number : ")))


if a >= b and  a >= c:
    greatest = a
elif b >= c 