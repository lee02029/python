from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 26:
        print("[0] {0}번쨰 {1}분".format(i,time))
        cnt += 1
    else:
        print("[0] {0}번쨰 손님".format(i,time))

print("총 탑승 승객 {}".format(cnt))