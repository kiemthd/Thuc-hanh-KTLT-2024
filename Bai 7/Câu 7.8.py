print('Hoàng Thanh Kiếm MSSV 235752021610003')
def ghi_danh_sach_vao_tep(ten_tep, danh_sach):
    try:
        with open(ten_tep, 'w', encoding='utf-8') as file:
            for item in danh_sach:
                                file.write(str(item) + '\n')
        print(f"Đã ghi nội dung danh sách vào tệp {ten_tep}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
danh_sach = ["Đào", "Quang", "Huy", "2005"]
ten_tep = "D:\Thực hành lập trình\Bài 7 Thao tác trên tập tin và thư mục trong Python\Câu 7.1.py"  # Đường dẫn của tệp cần ghi
ghi_danh_sach_vao_tep(ten_tep, danh_sach)
