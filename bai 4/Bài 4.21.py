print('Hoàng Thanh Kiếm MSSV 235752021610003')
def kiem_tra_chia_het_cho_5(chuoi_nhi_phan):
  """Kiểm tra và in các số nhị phân chia hết cho 5 trong một chuỗi

  Args:
    chuoi_nhi_phan: Chuỗi các số nhị phân cách nhau bởi dấu phẩy
  """
  # Tách chuỗi thành danh sách các số nhị phân
  danh_sach_so_nhi_phan = chuoi_nhi_phan.split(',')
  # Tìm và in các số chia hết cho 5
  ket_qua = []
  for so_nhi_phan in danh_sach_so_nhi_phan:
    # Chuyển đổi số nhị phân thành số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # Kiểm tra chia hết cho 5
    if so_thap_phan % 5 == 0:
      ket_qua.append(so_nhi_phan)
  # In kết quả
  print(','.join(ket_qua))
# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập chuỗi các số nhị phân: ")
# Gọi hàm kiểm tra
kiem_tra_chia_het_cho_5(chuoi_nhap)
