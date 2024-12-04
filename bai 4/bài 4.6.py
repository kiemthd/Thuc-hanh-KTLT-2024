print('Hoàng Thanh Kiếm MSSV 235752021610003')
ho_ten = input("Họ tên của mi là chi:")

#Tim vị trí của khoảng trắng(giả sử họ và tên chỉ con cách nhau
# bởi một khoảng trắng
vi_tri_khoang_trang = ho_ten.find(" ")

# Tách họ và tên
ho = ho_ten[:vi_tri_khoang_trang]
ten = ho_ten[vi_tri_khoang_trang+1:]

# In ra kết quả
print("Họ:", ho)
print("Tên:", ten)
