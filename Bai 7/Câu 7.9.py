print('Hoàng Thanh Kiếm MSSV 235752021610003')
def sao_chep_tep(tep_nguon, tep_dich):
    try:
        with open(tep_nguon, 'r', encoding='utf-8') as file_nguon:
            noi_dung = file_nguon.read()
        with open(tep_dich, 'w', encoding='utf-8') as file_dich:
            file_dich.write(noi_dung)
        print(f"Đã sao chép nội dung từ tệp {tep_nguon} sang tệp {tep_dich}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
tep_nguon = "source.txt"  
tep_dich = "destination.txt"  
sao_chep_tep(tep_nguon, tep_dich)
