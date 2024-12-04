print('Hoàng Thanh Kiếm MSSV 235752021610003')
chuoi = input("Nhập chuỗi đi thằng tê: ")
chuoi_moi = ""

for ky_tu in chuoi:
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu

print("Chuỗi mới: ", chuoi_moi)
