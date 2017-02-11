a = ["1", 1, "1", 2]
b = []

# Solution 1
for i in a:
    if i not in b:
        b.append(i)
print b


# Solution 2
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

# Solution 3
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

