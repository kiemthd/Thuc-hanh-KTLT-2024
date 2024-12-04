print('Hoàng Thanh Kiếm MSSV 235752021610003')
def tinh_so_du(nhat_ky):

  so_du = 0  
  for giao_dich in nhat_ky:  
    loai_giao_dich, so_tien = giao_dich.split()
      so_tien = int(so_tien) n
    if loai_giao_dich == 'D':  
      so_du += so_tien  
    elif loai_giao_dich == 'W':  
      so_du -= so_tien  
  return so_du  

# Nhập nhật ký giao dịch từ người dùng
nhat_ky = []  
while True:
  giao_dich = input("Nhập giao dịch (D <số tiền> hoặc W <số tiền>, nhập 'quit' để kết thúc): ")
  if giao_dich.lower() == 'quit':  
    break
  nhat_ky.append(giao_dich)  

# Tính số dư và in kết quả
so_du_cuoi = tinh_so_du(nhat_ky)  
print("Số dư cuối cùng của tài khoản:", so_du_cuoi)  
