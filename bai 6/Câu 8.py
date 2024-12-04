
balance = 10000000000
def display_menu():
    """Hiển thị menu các tùy chọn."""
    print("\n===== ATM Menu =====")
    print("1. Xem số dư")
    print("2. Rút tiền")
    print("3. Nạp tiền")
    print("4. Thoát")
def check_balance():
    """Kiểm tra và in số dư hiện tại."""
    print(f"Số dư hiện tại của bạn là: {balance} VND")
def withdraw_money():
    """Hàm để rút tiền."""
    global balance
    amount = float(input("Nhập số tiền muốn rút: "))
    if amount > balance:
        print("Số dư không đủ để thực hiện giao dịch này.")
    elif amount <= 0:
        print("Số tiền rút phải lớn hơn 0.")
    else:
        balance -= amount
        print(f"Bạn đã rút {amount} VND. Số dư mới là: {balance} VND")
def deposit_money():
    """Hàm để nạp tiền."""
    global balance
    amount = float(input("Nhập số tiền muốn nạp: "))
    if amount <= 0:
        print("Số tiền nạp phải lớn hơn 0.")
    else:
        balance += amount
        print(f"Bạn đã nạp {amount} VND. Số dư mới là: {balance} VND")
def main():
    """Chạy chương trình ATM."""
    while True:
        display_menu()
        choice = input("Chọn một tùy chọn (1-4): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
# Chạy chương trình
main()
