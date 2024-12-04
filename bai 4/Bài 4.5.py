print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Nhập danh sách các từ từ bàn phím
danh_sach = input("Nhập danh sách các từ: ").split()

# Đảo ngược thứ tự của danh sách
danh_sach.reverse()

# In ra danh sách các từ đã đảo ngược
print("Danh sách các từ sau khi đảo ngược: ", end="")
for sach in danh_sach:
    print(sach, end=" ")
