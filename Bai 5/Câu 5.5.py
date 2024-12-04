print('Hoàng Thanh Kiếm MSSV 235752021610003')
import mymodule

n = int(input("Nhập số lượng phần tử trong danh sách: "))
lst = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng các hàm trong mymodule
sorted_lst = mymodule.sort_list(lst)  
max_value = mymodule.find_max(lst)
