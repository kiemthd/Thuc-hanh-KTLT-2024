print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Nhập chuỗi các số nhị phân từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân, cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành các số nhị phân
binary_numbers = input_string.split(',')

# In ra các giá trị đã nhập
print("Các số nhị phân đã nhập:")
for binary in binary_numbers:
    print(binary)
