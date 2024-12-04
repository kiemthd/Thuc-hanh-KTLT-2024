print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi các từ tiếng Anh: ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Sắp xếp danh sách các từ theo thứ tự từ điển
sorted_words = sorted(words)

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
for word in sorted_words:
    print(word)
