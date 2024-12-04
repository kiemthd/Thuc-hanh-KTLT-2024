print('Hoàng Thanh Kiếm MSSV 235752021610003')
def dem_chu_hoa_thuong(cau):


  so_chu_hoa = 0  # Biến lưu số lượng chữ hoa
  so_chu_thuong = 0   # Biến lưu số lượng chữ thường

  for ky_tu in cau:  # Duyệt qua từng ký tự trong câu
    if ky_tu.isupper():  # Kiểm tra xem ký tự có phải là chữ hoa không
      so_chu_hoa += 1  # Nếu là chữ hoa, tăng số chữ hoa lên 1
    elif ky_tu.islower():  # Kiểm tra xem ký tự có phải là chữ thường không
      so_chu_thuong += 1  # Nếu là chữ thường, tăng số chữ thường lên 1

  return so_chu_hoa, so_chu_thuong  # Trả về tuple chứa số chữ hoa và chữ thường

# Nhập câu từ người dùng
cau = input("Nhập một câu: ")

# Gọi hàm đếm và in kết quả
so_chu_hoa, so_chu_thuong = dem_chu_hoa_thuong(cau)
print("Số chữ hoa là:", so_chu_hoa)
print("Số chữ thường là:", so_chu_thuong)
