#!/usr/bin/python3

my_list = ["strings", 15, 14.5, True]
my_list.append(6)
print(my_list)
my_list.insert(1, "insert")
print(my_list)
my_list.remove(15)
print(my_list)
last_value = my_list.pop()
print(my_list)
print(last_value)


my_list_one = [1,9,22,6,8,65,14,99]
my_list_one.sort(reverse = True)
print(my_list_one)

my_list_two = [27, 7]
my_list_one.extend(my_list_two)
print(my_list_one)