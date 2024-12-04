print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Mở tệp với chế độ đọc
with open('D:/Thực hành lập trình/Bài 7 Thao tác trên tập tin và thư mục trong Python/Câu 7.2.py', 'r', encoding='utf-8') as file:
    # Khởi tạo các biến để đếm số dòng, số từ và số ký tự
    line_count = 0
    word_count = 0
    char_count = 0
    
    # Đọc từng dòng trong tệp
    for line in file:
        line_count += 1  # Tăng số dòng lên 1 cho mỗi dòng
        word_count += len(line.split())  # Đếm số từ trong dòng (split() chia theo khoảng trắng)
        char_count += len(line)  # Đếm số ký tự trong dòng

    # In kết quả
    print(f"Số dòng trong tệp: {line_count}")
    print(f"Số từ trong tệp: {word_count}")
    print(f"Số ký tự trong tệp: {char_count}")
