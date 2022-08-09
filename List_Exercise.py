#Exercise 1
info = ['karl', '100', 'Red', 'Mangoes']
info.reverse()
print(info)

#Exercise 2
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [list1 +list2 for list1, list2 in zip(list1, list2)]
print(list3)

#Exercise 3
list1 = [10, 20, 4]
list1.sort()
print(sorted(list1)[-2])

list2 = [70, 11, 20, 4, 100]
list2.sort()
print(sorted(list2)[-2])

#Exercise 4
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)

#Exercise 5
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

#Exercise 6
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
def countX(lst, x):
    return lst.count(x)
print('{} has occurred {} times'.format(x, countX(lst, x)))

#Exercise 7
list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]
res = remove_value(list1, 20)
print(res)

#Exercise 8
age = [10, 3, 45, 67, 89.0, 45]
middle_index=int((len(age)/2))
print(age[middle_index])
