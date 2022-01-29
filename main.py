from Lists import *
from Dicts import *
from Tuples import *

l = Lists ([1, 2, 3, 45, 6])

# print(l.l_insert())
# print(l.l_count())
print(l.l_reverse())
# print(l.l_copy())

d = Dicts({"a": 12,
               "b": 13,
               "c": 14,
               "d": 15})
#
#
d.my_keys()
d.my_values()
t = Tuples((1,2,5,3,5,2,5), v=0)

print(t.my_count(5))
t.my_index(2)



