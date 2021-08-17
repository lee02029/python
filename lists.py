friends =  ["Kevin", "Karen" , "Jim"]

print(friends[1 : 3])
friends.insert(1,"mike")
print(friends)
friends.append("kim")
print(friends)
print(friends.count("kim"))
num_list = [5,3,4,1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

num_list = [5,2,3,4]
mix_list = [1,48]

num_list.extend(mix_list) 
print(num_list)