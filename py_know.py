"""string
"""
s = "about"
s.replace("a", "", 1)
sum([2, 3, 4])
len([2, 3, 4])
# index of letter in a string, 1
"abefere".find("b") 
# -1
"abefere".find("g") 
# substring, "befere"
"abefere"[1:]

"""dict
"""
dic = {"a":1, "b":2}
for key, value in dic.items():
    print(key, value)

dic.get("c", 0) # 0 is the default value
# note that you cannot use this: dic.get("c", default_value = 0)
# because dict.get() does not take keyword argument

"""list
"""
# note that if you print(a.remove("a")), it will be None
# this is true for most the methods related to list
# they just do the operations but return None 

a=["a", "c"]
a.remove("a")
a.append("d")
a.insert(1, "f")

# remove through index
a.pop(1)
# or 
del a[1]

# remove the last one
a.pop()

# clear a list
a.clear()

# reverse order
a.reverse()

# sort, by default ascending
a.sort(reverse=False)
# sort, descending
a.sort(reverse=True)

# join
b = ["c", "d"]
# this is wrong:
[a, b]
# this is correct:
a + b

# count the frequency of an element
b.count('c') == 1

# index of the first occurence of an element
b.index("c") == 0

"""numbers
"""
max(2, 1)
abs(-10) == 10
max([2, 9, 10])
len(str(20)) == 2

# [5, 4, 3, 2, 1, 0]
# start, stop, step
range(5, -1, -1)

"""set
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set.intersection(set1, set2)