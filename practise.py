# Define a list 'a' with some duplicate and unique elements
# a = [10,24,35,24,89,67,45,89]
#
# # Create an empty set to store duplicate items and an empty list for unique items
# dup_items = set()
# uniq_items = []
#
# # Iterate through each element 'x' in the list 'a'
# for x in a:
#     # Check if the current element 'x' is not already in the set 'dup_items' (it's a duplicate check)
#     if x not in dup_items:
#         # If 'x' is not a duplicate, add it to the 'uniq_items' list
#         uniq_items.append(x)
#         # Add 'x' to the 'dup_items' set to mark it as a seen item
#         dup_items.add(x)
#
# # Print the set 'dup_items' which now contains the unique elements from the original list 'a'
# print(uniq_items)
# numbers = [1,2,3,2,3,3,5,6,7,5,5,6,8]
# duplicates = [number for number in numbers if numbers.count(number) >1]
# unique_duplicates = list(set(duplicates))
# print(unique_duplicates)


# lst1 = [3, 1, 5, 1, 10, 3, 5, 10,2,4]
# duplicates = set()
# for i in lst1:
#     if i not in duplicates:
#         duplicates.add(i)
# print(duplicates)
# numbers = [1,2,4,5,6,2,3,4,5,6,7]
# duplicates = set()
# for i in numbers:
#     if i not in duplicates:
#         duplicates.add(i)
# print(duplicates)


# num = [23,12,23,4,53,4,5,12,12,23]
# duplicates = set()
# for i in num:
#     if i not in duplicates:
#         duplicates.add(i)
# print(duplicates)


# list = [1,2,3,4,5,12,3,4,5,6]
# dup_items = set()
# unique_items = []
# for i in list:
#     if i not in dup_items:
#         unique_items.append(i)
#         dup_items.add(i)
# print(dup_items)

# list = [1,2,3,4,5,6,7]
# if not list:
#     print("list is empty")
# else:
#     print("not empty list")

# list1 = [1,2,3,4,5,6,7,8,9]
# new_list = list(list1)
# print(new_list)
# print(list1)
# for x in list1:
#     print(x)
#
#
#     print(list1)

# def comm_data(x,y):
#
#     for i in x:
#         for j in y:
#             if i == j:
#                 result = True
#             else:
#                 result = False
#     return result
# print(comm_data([1,2,3,4,5,6],[20,41,61,7,89]))

# colors = ['red','white','green','yellow','brown','black']
# # numbers = [1, 9, 8, 4, 9, 2, 9]
#
# # Remove all occurrences of 9
# colors = [ele for ele in colors if ele != 'green']
#
# print("List after removing all green:", colors)

# home =['tv','fridge','humans','bed','kitchen','tree']
# home = [things for things in home if things != 'tree']
# print("things that  belong to home:",home)


# def max_list(list):
#     max = list[0]
#     for x in list:
#         if x > max:
#             max = x
#     return max
# print(max_list([24,134,56,356,789,1,2]))

# a = [23,12,34,35,45,23,12,45,56,34,23,56,45,56,1,2,3,4,5]
# dup_items = set()
# unique_items = []
# for x in a:
#     if x not in unique_items:
#         unique_items.append(x)
#         dup_items.add(x)
# print(unique_items)

# l1 = [1,2,3,4,5]
# if not l1:
#     print("empty")
# else:
#     print("not empty")
# tuple
# x = (23,34,56,7,8)
# print(x)
# print(type(x))


# x = ("hello",'False',1,2,2.4)
# print(x)
#
# x = (1,23,3,45,5,6,7,89,80)
# x = 3
# print(x)
# Tuple = (1,2,3,4,5)
# print(Tuple)
# print(len(Tuple))
# print(type(Tuple))
# numb = (1,3,2,4,5,2,3,4,6,78,9,4,3,8,90,23,24,56,78,56)
# for hello in numb:
#     if numb.count(hello) > 1:
#         print(hello)
# letters = ("peer","poor","laptop")
# for i in letters:
#     if letters.count(i) >2:
#         print(i)
# from collections import Counter
#
# tup = (1, 3, 4, 32, 1, 1, 1, 31, 32, 12, 21, 2, 3)
# for a, b in Counter(tup).items():
#     if b > 1:
#         print(f"Repeated: {a}")
#
# from  collections import Counter
# aaa = (1, 3, 4, 32, 1, 1, 1, 31, 32, 12, 21, 2, 3)
# for y, x in Counter(aaa).items():
#     if x > 1:
#         print(y)

# from  collections import Counter
# aaa = (1, 3, 4, 32, 1, 1, 1, 31, 32, 12, 21, 2, 3)
# for x , y in Counter(aaa).items():
#     if y > 1:
#         print(x)
# from collections import Counter
# abc = (1,2,3,4,5,6,7,81,3,24,56,34,52,1,34,43,2,4,6,7,1)
# # for x, y in Counter(abc).items():
# #     if y >2:
# #         print(x)
# print(tuple(abc))
#dictonary is used to implement key value pair in python.dictionary is a data type in python which is simulate the
#real life data arrangmet where some special keys exist for some particuar value
# ele = ['laptop','mouse','keyboard']
# color = ['black','white','red']
# mer = dict(zip(ele,color))
# print(mer)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict4 = {'one': 1, 'Two': 2, 'Three': 3}
#
# # dict3 = dict1.copy()
# # dict3.update(dict2)
# # print(dict3)
# dict3 = {**dict1,**dict2,**dict4}
# print(dict3)
#
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80,
#                 "chemistry":90,
#             "grade":{
#                 "physics":"A",
#                 "history":"A+",
#                 "chemistry":"O"
#
#             }
#             }
#         }
#     }
# }
#
# print(sampleDict['class']['student']['marks']['physics'])
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res = dict.fromkeys(employees, defaults)
# print(res)
#
# # Individual data
# # print(res["Kelly"])


#initializ value
# key = ['home','temple']
# value = {'light':'bulb','fan':'oriented','statue':'ram'}
# in_one = dict.fromkeys(key,value)
# print(in_one)
# print(in_one['home'])
# print(in_one['temple'])
# sample_dict = {
#     'name':'samir',
#     'age':27,
#     'color':'brown',
#     'live':'kalyan'
#
# }
# if 'age' in sample_dict.values():
#     print("yes")
# else:
#     print("no")

#Function - a fun is a block of organised, reusable code that is use to perform single, related action.
#rules - fun begin with the keyword def followed by fun name and parenthesis. any input parameter and argument sholud be
#placed within parathesis.you can also define parameter in parenthesis.
# the first statement in function can be an optional statemnet.code block within every fun strt with the colon. and is indented.

# def getname(a,b):
#     if a<b:
#         print("yes")
#     else:
#         print("no")
# a = 18
# b = 20
#
# getname(a,b)
#
# c = 20
# d = 17
# getname(c,d)

# def sub(a,b):
#     print(a-b)
# a = 78
# b = 30
# sub(a,b)
# def mul(c,d):
#     print(c*d)
# c = 21
# d = 12
# mul(c,d)
# def add(e,f):
#     print(e+f)
# e = 34
# f = 25
# add(e,f)


# def greet(name,message= "hello"):
#     print(f"{message},{name}")
# greet("Alice","Hii")
# greet("Bob")
# greet(" ","Guys")

# def get(name,lastname="salekar"):
#     print("my name is:",name,lastname)
# get("ramesh")
# get("suresh")


# def student(firstname, lastname="hello"):
# #     print(firstname, lastname)
#
#
# # Keyword arguments
# # student(firstname='Geeks')
# # student(lastname='Practice', firstname='Geeks')
#
# def calculator():
#     def add():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a+b)
#     def mul():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a*b)
#     def div():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a/b)
#     def sub():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a-b)
#     def avg():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a+b/2)
#     def per():
#         a = int(input("enter the value"))
#         b = int(input("enter the value"))
#         print(a+b/2)
#     oper = input("enter the operation")
#     if oper == "add":
#         add()
#     elif oper == "mul":
#         mul()
#     elif oper == "sub":
#         sub()
#     elif oper == "div":
#         div()
#     elif oper == "avg":
#         avg()
#     elif oper == "per":
#         per()
#     return oper
# calculator()
# def amir(firstname,middlename,lastname):
#     print(firstname,middlename,lastname)
# amir("samir","ramesh","salekar")

#variable length arguments
# def samir(*arge):
#     for i in arge:
#         print(i)
# samir(20,34,56,45,78)
# samir(45,67,89,45)


#return
# def samir(c,d):
#     mul = c*d
#     add = c+d
#     return mul,add
# sam = samir(56,34)
# print(sam)
#default arguments
# def tile (a ="water",b="cement"):
#     print("to make a tile use:",a,b)
# tile(a="soil")

# def show_employees(name,salary=10000):
#     print("name:",name,"salary:",salary)
# show_employees("samir",12000)
# show_employees("pallavi")
#nested fun
# def outer_fun(a,b):
#     mul = a*b
#     def inner_fun(a,b):
#         return a+b
#     add = inner_fun(a,b)
#     return add+5
# result = outer_fun(20,30)
# print(result)

# def mouse (a,b):
#     print("sum of all num is:",a+b)
# mouse(23,34)
# robot = mouse
# robot(23,34)

# def fun1(num):
#     return num + 25
#
# sam = fun1(5)
# print(sam)

# def display_person(*args):
#     for i in args:
#         print(i)
#
# display_person(name="Emma", age="25")


# def isgreater(a,b,f):
#     if a>b and f<a and f>b:
#         print("first value is greater")
#     else:
#         print("third value is greater")
#
# def issmaller(c,d):
#     if c<d:
#         print("hello")
#     else:
#         print("by")
#
# def add(x,y,z):
#     print(x+y+z)
#     print(x*y*z)
# add(23,45,78)
# isgreater(40,20,34)
# isgreater(20,30,78)
# issmaller(23,57)


# #map function
# def triple_x(a):
#     return a*6
# def sq(a):
#     return a*a
#
#
#
#
# #making a list with variable animal
# animal = [1,2,3,4,5,6,7,8,9,10]
# book = list(map(triple_x,animal))
# print(book)
# suare = list(map(sq,animal))
# print(suare)

# list1 = [1,2,3,4,5]
# list2= [6,7,7]
# list3 = [8,9,10]
# add_3 = list(map(lambda x,y,z:x+y+z , list1,list2,list3))
# print(add_3)

# color = ['Red', 'Blue', 'Black', 'White', 'Pink']
# print("original list")
# print(color)
# print("after litfy the list")
# num = list(map(list,color))
# print(num)


# def change_case(s):
#     return str(s).upper(), str(s).lower()
# list1 = ['a','s','d','e','r','t']
# UPPEr_lower_char = list(map(change_case,list1))
# print(UPPEr_lower_char)

# def add_sub(x,y):
#     return x+y,x-y,x*y,x/y
# list1 = [23,45,23,67]
# list2 = [10,23,12,34]
# result = list(map(add_sub,list1,list2))
# print(result)
#filter function

#
# def elements (s):
#     return s<=5
# list1 = [1,2,3,4,5,6,7,8]
# less_than_equal_to_5 = list(filter(elements,list1))
# print(less_than_equal_to_5)


# names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
#
# def is_vowel (s):
   # return s[0].upper() in ['a','e','i','o','u']
# hllo = list(filter(is_vowel,names))
# print(hllo)

#Define a list of city-population tuples
# cities = [
#     ("New York", 8500000),
#     ("Los Angeles", 4000000),
#     ("Chicago", 2700000),
#     ("Houston", 2300000),
#     ("Phoenix", 1600000),
#     ("Philadelphia", 1500000),
#     ("San Antonio", 1500000),
# ]
#
# print("list of city and population:")
# print(cities)
# # Define a function to check if a city has a population greater than 2 million
# def has_population_greater_than_two_million(city_population):
#     return city_population[1] > 2000000
#
# # Use the filter function to extract cities with a population greater than two million
# million_plus_cities = list(filter(has_population_greater_than_two_million, cities))
#
# print("\nExtract cities with a population greater than 2 million:")
# # Print the extracted cities
# print(million_plus_cities)
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#
# # Display the original list of tuples to the console
# print("Original list of tuples:")
# print(subject_marks)
#
# # Sort the 'subject_marks' list of tuples based on the second element of each tuple (the marks),
# # using a lambda function as the sorting key to extract the second element
# subject_marks.sort(key=lambda x: x[1])
#
# # Display the sorted list of tuples to the console
# print("\nSorting the List of Tuples:")
# print(subject_marks)
# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# sorted_list = sorted(models,key=lambda x:x['model'])
# print(sorted_list)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_number = list(filter(lambda x: x % 2 == 0,list1))
# print(even_number)
# odd_number = list(filter(lambda x:x % 2 !=0, list1))
# print(odd_number)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sqr = list(map(lambda x : x**2,list1))
# print(sqr)
# cube1 = list(map(lambda x: x**3,list1))
# print(cube1)


# starts_with = lambda x : True if x.startswith ('p') else False
# print(starts_with('python'))
# print(starts_with('java'))