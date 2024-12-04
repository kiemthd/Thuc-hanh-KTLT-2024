print('Hoàng Thanh Kiếm MSSV 235752021610003')
def loc_so_le(danh_sach):


  so_le = []  # Khởi tạo danh sách rỗng để lưu các số lẻ
  for so in danh_sach:  # Duyệt qua từng số trong danh sách
    if so % 2 != 0:  # Kiểm tra nếu số đó là số lẻ (số không chia hết cho 2)
      so_le.append(so)  # Nếu là số lẻ, thêm vào danh sách so_le
  return so_le  # Trả về danh sách các số lẻ

# Nhập danh sách từ người dùng
danh_sach_nhap = input("Nhập danh sách các số (cách nhau bằng dấu phẩy): ")

# Chuyển đổi chuỗi nhập vào thành một danh sách các số nguyên
danh_sach = [int(so) for so in danh_sach_nhap.split(',')]  # Tách chuỗi và chuyển thành danh sách số nguyên

# Gọi hàm lọc và in kết quả
ket_qua = loc_so_le(danh_sach)  # Gọi hàm lọc các số lẻ
print("Danh sách các số lẻ:", ket_qua)  # In danh sách các số lẻ
