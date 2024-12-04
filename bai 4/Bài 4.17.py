print('Hoàng Thanh Kiếm MSSV 235752021610003')
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

print(f"Các số nguyên dương nhỏ hơn {n} có tổng các ước số lớn hơn chính nó:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
