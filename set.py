my_set = {1,2,3,3,4}
print(my_set)

python = set(["kim","lee"])
java = {"kk","ll","lee"}

#교집합
print(python & java)
print(python.intersection(java))

#합집합
print(python | java)
print(python.union(java))

#차집합
print( python - java)
print(java.difference(python))

#제거
python.remove("kim")
print(python)