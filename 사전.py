#cabi = {3:"lee" , 100:"kim"}
#print(cabi.get(5))

cabi = {"A-3":"lee", "B-100":"lim"}

del cabi["A-3"]
print(cabi.keys())
print(cabi.values())
print(cabi.items())
cabi.clear()
print(cabi)
