print('Hoàng Thanh Kiếm MSSV 235752021610003')
import binary_search  
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []
    print("Nhập các phần tử:")
    for i in range(n):
        lst.append(int(input(f"Phần tử {i + 1}: ")))
    lst.sort()
    value = int(input("Nhập giá trị cần tìm: "))
    result = binary_search.binary_search(lst, value)
    if result != -1:
        print(f"Giá trị {value} được tìm thấy tại chỉ mục {result}.")
    else:
        print(f"Giá trị {value} không có trong danh sách.")
if __name__ == "__main__":
    main()
