"""
このファイルに解答コードを書いてください
"""
from collections import OrderedDict

# input
d = {}
m = 0

while True:
    s = input().split(':')
    if len(s) == 1:
        m = int(s[0])
        break
    key = int(s[0])
    value = s[1]
    d[key] = value

# sort
d = OrderedDict(
    sorted(d.items(), key=lambda x: x[0])
)

# calc result
result = ""
for key, val in d.items():
    if m % key == 0:
        result += val


# display result
if result == "":
    print(m)
else:
    print(result)
