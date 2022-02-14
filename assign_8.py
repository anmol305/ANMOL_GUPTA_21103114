set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
# solution to part a)
new_set_1 = set1 ^ set2
print(new_set_1)
# solution to part b)
a = set1 - set2
b = a - set3

c = set2 - set1
d = c - set3

e = set3 - set1
f = e - set2

new_set_2 = b | d | f
print(new_set_2)
# solution to part c)
a = (set1 | set3) - set2

b = (set1 | set2) - set3

c = (set2 | set3) - set1
new_set_3 = a | b | c
print(new_set_3)
# solution to part d)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
new_set_4 = a - set1
print(new_set_4)
# solution of part e)
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = a - set1
new_set_5 = b - (set2 & set3)
print(new_set_5)
