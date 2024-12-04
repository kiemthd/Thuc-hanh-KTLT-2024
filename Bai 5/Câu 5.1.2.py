print('Hoàng Thanh Kiếm MSSV 235752021610003')
# File: main.py

import mymath as mt  # Nhập module mymath với tên tắt là mt

# Danh sách các giá trị
values = [2, 4, 6, 8, 10]

# Tính bình phương của từng giá trị trong danh sách
print('Squares:')
for v in values:
    print(mt.square(v))  # Gọi hàm square từ mymath (sử dụng tên tắt mt)

# Tính lập phương của từng giá trị trong danh sách
print('Cubes:')
for v in values:
    print(mt.cube(v))  # Gọi hàm cube từ mymath (sử dụng tên tắt mt)

# Tính trung bình của danh sách
print('Average: ' + str(mt.average(values)))  # Gọi hàm average từ mymath 
