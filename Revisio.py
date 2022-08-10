# Exercise 1

str = "Hello World"
split = str.split()
res = list(reversed(split))
res =" ".join(res)
print(res)

#Exercise 2

list1 = [10, 23, 23, 5, 67, 10]

unique = set(list1)
print(unique)

#Exercise 3

import string
checker = [0,0,0,0]
password="1EggPerD@y"
for i in password:
    if i.isupper():
        checker[0] = 1
    if i.islower():
        checker[1] = 1
    if i.isnumeric():
        checker[2] = 1
    if i in string.punctuation:
        checker[3] = 1
print("True") if 0 not in checker else print("False")


# Exercise 4

list_id = [[4,1,6], [7,9], [8,9,2,4]]

for x in list_id:
    x.sort(reverse=True)
print(list_id)

#Exercise 5

test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
res = []
for sub in test_list:
    res.append([[ele, sub[-1]] for ele in sub[:-1]])
print(res)

#Exercise 6


str1 = "%There &are three( students$ and& 1 trainer!"
new = ""
for x in str1:
    if x in string.punctuation:
        new += string.punctuation[2]
    else:
        new += x
print(new)

#Exercise 7

str1 = "My mum has a 10 year old dog and 2 fishes"

res = [x for x in str1 if x.isdigit()]
res = ''.join(res)
print(res)

# Exercise 8

name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']
new_list = list(filter(None, name_list))
print(new_list)