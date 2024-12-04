print('Hoàng Thanh Kiếm MSSV 235752021610003')
def fibonacci_less_than(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Tạo danh sách các số Fibonacci nhỏ hơn n
fibonacci_numbers = fibonacci_less_than(n)

# In ra danh sách các số Fibonacci
print(f"Các số Fibonacci nhỏ hơn {n}:")
print(fibonacci_numbers)
