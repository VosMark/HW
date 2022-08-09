#Exercise 1
def get_middle_three_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("CopsArtList")

#Exercise 2
def append_middle(s1, s2):
    print("Old:", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("Now:", x)

append_middle("Aunt", "Sister")
