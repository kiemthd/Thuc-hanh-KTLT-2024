print('Hoàng Thanh Kiếm MSSV 235752021610003')
def dem_so_dong(ten_tep):
    try:
        with open(ten_tep, 'r', encoding='utf-8') as file:
            so_dong = sum(1 for line in file)
        return so_dong
    except FileNotFoundError:
        print(f"Tệp {ten_tep} không tồn tại!")
        return 0
ten_tep = "D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.1.py"
so_dong = dem_so_dong(ten_tep)
if so_dong > 0:
    print(f"Số dòng trong tệp {ten_tep} là: {so_dong}")
