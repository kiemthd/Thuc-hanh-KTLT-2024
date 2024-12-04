print('Hoàng Thanh Kiếm MSSV 235752021610003')
def print_pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1)  # Khởi tạo hàng với tất cả các giá trị là 1
        for j in range(1, i):  # Tính các giá trị trung gian
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)))  # In ra từng hàng

# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# In n dòng đầu tiên của tam giác Pascal
print_pascals_triangle(n)
