lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "karen", "Jim", "Oscar", "Mike"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.remove("Jim")
friends.insert(1, "Kelly")
print(friends)
print(friends.index("Mike"))
