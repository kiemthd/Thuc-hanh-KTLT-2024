class BankAccount:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
    def verify_pin(self, entered_pin):
        return entered_pin == self.pin
    def deposit(self, amount):
        self.balance += amount
        print(f"Bạn đã gửi {amount} đồng. Số dư hiện tại là {self.balance} đồng.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Bạn đã rút {amount} đồng. Số dư còn lại là {self.balance} đồng.")
        else:
            print("Số dư không đủ.")
    def check_balance(self):
        print(f"Số dư hiện tại của bạn là {self.balance} đồng.")
account = BankAccount("Nguyễn Văn A", "123456789", 1000000, 1234)
while True:
    pin = int(input("Nhập PIN của bạn: "))
    if account.verify_pin(pin):
        break
    else:
        print("PIN không đúng. Vui lòng nhập lại.")
while True:
    print("\nChọn chức năng:")
    print("1. Kiểm tra số dư")
    print("2. Rút tiền")
    print("3. Gửi tiền")
    print("4. Thoát")
    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        account.check_balance()
    elif choice == 2:
        amount = int(input("Nhập số tiền muốn rút: "))
        account.withdraw(amount)
    elif choice == 3:
        amount = int(input("Nhập số tiền muốn gửi: "))
        account.deposit(amount)
    elif choice == 4:
        break
    else:
        print("Lựa chọn không hợp lệ.")
