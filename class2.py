class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("입금 금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족하여 출금할 수 없습니다.")
        elif amount <= 0:
            print("출금 금액은 0보다 커야 합니다.")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")

    def display_balance(self):
        print(f"{self.owner}님의 현재 잔액: {self.balance}원")