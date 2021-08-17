customer = "lee"
index = 5
while index >= 1:
    print("{0},커피준비 {1}남음".format(customer,index))
    index -= 1
    if index == 0:
        print("폐기처분")


absent = [2, 5]
for student in range(1,11):
    if student in absent:
        continue
    print("{0}, read".format(student))

