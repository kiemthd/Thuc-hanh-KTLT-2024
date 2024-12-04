print('Hoàng Thanh Kiếm MSSV 235752021610003')
def dem_chu_cai_va_chu_so(cau):


  so_chu_cai = 0  
  so_chu_so = 0   

  for ky_tu in cau: 
    if ky_tu.isalpha():  
      so_chu_cai += 1  
    elif ky_tu.isdigit(): 
      so_chu_so += 1  

  return so_chu_cai, so_chu_so  

# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

# Gọi hàm đếm và in kết quả
so_chu_cai, so_chu_so = dem_chu_cai_va_chu_so(cau)
print("Số chữ cái là:", so_chu_cai)
print("Số chữ số là:", so_chu_so)
