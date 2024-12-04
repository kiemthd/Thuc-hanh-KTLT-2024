print('Hoàng Thanh Kiếm MSSV 235752021610003')
# File: main.py

import mymath
values = [2, 4, 6, 8, 10]
print('Squares:')
for v in values:
    print(mymath.square(v)) 
print('Cubes:')
for v in values:
    print(mymath.cube(v))  

# Tính trung bình của danh sách
print('Average: ' + str(mymath.average(values)))  

