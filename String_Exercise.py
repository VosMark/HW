#Exercise 1
def get_middle_three_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("CopsArtList")

#Exercise 2

def append_middle(s1, s2):
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("s3:", x)

append_middle("Aunt", "Sister")

#Exercise 3

def s3(s1, s2):
    first_char = s1[0] + s2[0]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("s3=", res)

s1 = "America"
s2 = "Japan"
s3(s1, s2)

#Exercise 4
s1 = "Yn"
s2 = "PYnative"
res = True
for i in s1:
    if i in s2:
        res = True
    else:
        res = False
        break
print(res)

s1 = "Ynf"
s2 = "PYnative"
res = True
for i in s1:
    if i in s2:
        res = True
    else:
        res = False
        break
print(res)

#Exercise 5
str1 = "Emma-is-a-data-scientist"

x = str1.split(sep="-")
print(x[0] + ", " + x[-1])


#Exercise 6
txt = "Hello World"[::-1]
print(txt)

#Exercise 7
str1 = "Emma is a data scientist who knows Python. Emma works at google."
result = str1.rfind("Emma")
print("Last occurrence of Emma starts at index " + str(result))
