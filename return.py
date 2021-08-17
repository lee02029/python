def open():
    print("생성")

def deposit(balance,money):
    print("입금이 완료되었습니다{0}원".format(balance +money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료 {0}".format(balance-money))
        return balance-money
    else:
        print("stop {0}".format(balance))
        return balance


balance = 0
balance = deposit(balance,3000)
balance = withdraw(balance,2000)
