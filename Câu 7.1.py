print('Hoàng Thanh Kiếm MSSV 235752021610003')
with open('E:\Bài 7 Thao tác trên tập tin và thư mục trong Python\Câu 7.1.py', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        reversed_line = line[::-1]
        print(reversed_line)
