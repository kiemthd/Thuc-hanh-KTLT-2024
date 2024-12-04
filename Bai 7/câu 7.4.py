print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Đọc n dòng đầu tiên của tệp
def read_first_n_lines(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Đọc n dòng đầu tiên
        for i in range(n):
            line = file.readline()
            if line:  # Kiểm tra nếu dòng không rỗng
                print(line, end='')  # In ra dòng mà không có ký tự '\n' (vì readline() đã có '\n' ở cuối)
            else:
                break  # Dừng lại nếu tệp không đủ dòng

# Gọi hàm với đường dẫn tệp và số dòng cần đọc
file_path = 'D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.1.py'
n = 5  # Đọc 5 dòng đầu tiên
read_first_n_lines(file_path, n)
