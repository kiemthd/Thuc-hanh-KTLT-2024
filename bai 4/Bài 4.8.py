print('Hoàng Thanh Kiếm MSSV 235752021610003')
def tim_tu_dai_nhat(danh_sach_tu):
    """Tìm và in ra các từ dài nhất trong một danh sách các từ."""
    
    # Kiểm tra nếu danh sách trống
    if not danh_sach_tu:
        print("Danh sách trống! Không có từ nào để tìm.")
        return

    # Tìm độ dài lớn nhất của các từ
    do_dai_lon_nhat = max(len(tu) for tu in danh_sach_tu)
    
    # In ra các từ có độ dài bằng độ dài lớn nhất
    print("Các từ dài nhất:")
    for tu in danh_sach_tu:
        if len(tu) == do_dai_lon_nhat:
            print(tu)

# Nhập danh sách các từ từ bàn phím
danh_sach_tu = input("Nhập danh sách các từ: ").split()

# Gọi hàm để tìm và in ra các từ dài nhất
tim_tu_dai_nhat(danh_sach_tu)
