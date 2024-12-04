print('Hoàng Thanh Kiếm MSSV 235752021610003')
def noi_van_ban_vao_tep(ten_tep, noi_dung_moi):
    # Nối văn bản vào tệp
    with open(ten_tep, 'a', encoding='utf-8') as file:
        file.write(noi_dung_moi + '\n')  
    with open(ten_tep, 'r', encoding='utf-8') as file:
        noi_dung = file.read()  
        print("Nội dung tệp sau khi nối:")
        print(noi_dung)
ten_tep = 'D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.1.py'
noi_dung_moi = "Đào Quang Huy MSSV 235752021610051"
noi_van_ban_vao_tep(ten_tep, noi_dung_moi)
