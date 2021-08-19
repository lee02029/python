class Unit:
    def __init__(self, name, hp, damage):  #__init__ = 파이썬에서 쓰이는 생성자
        self.name = name
        self.hp = hp
        self.damage =damage
        print("{0}유닛이 생성".format(self.name))
        print("체력 {0},공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린",40, 5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름:{0}, 공력력:{1}".format(wraith1.name, wraith1.damage))  #멤버변수

wraith2 = Unit("뻬앗긴 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹상태입니다.".format(wraith2.name,))