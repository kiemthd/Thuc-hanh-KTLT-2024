print('Hoàng Thanh Kiếm MSSV 235752021610003')
import mymodule
n = int(input("Nhập số lượng phần tử trong danh sách: "))
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)
sorted_lst = mymodule.sort_list(lst) 
max_value = mymodule.find_max(lst)    
min_value = mymodule.find_min(lst)    
max_index = lst.index(max_value)
min_index = lst.index(min_value)
print("\nDanh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất trong danh sách:", max_value, "vị trí:", max_index)
print("Phần tử nhỏ nhất trong danh sách:", min_value, "vị trí:", min_index)
