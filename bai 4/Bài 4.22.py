print('Hoàng Thanh Kiếm MSSV 235752021610003')
def tim_so_chan_toan_chu_so(bat_dau, ket_thuc):


  so_chan = []
  for num in range(bat_dau, ket_thuc + 1):
    # Chuyển số thành chuỗi để kiểm tra từng chữ số
    chuoi_so = str(num)
    # Kiểm tra xem tất cả các chữ số có đều là số chẵn không
    if all(int(chu_so) % 2 == 0 for chu_so in chuoi_so):
      so_chan.append(str(num))

  return ', '.join(so_chan)

# Gọi hàm với khoảng từ 1000 đến 3000
ket_qua = tim_so_chan_toan_chu_so(1000, 3000)
print(ket_qua)
