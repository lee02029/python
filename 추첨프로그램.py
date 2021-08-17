from random import*
users = range(1,21)
users = list(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("{0}".format(winners[0]))
print("{0}".format(winners[1:]))