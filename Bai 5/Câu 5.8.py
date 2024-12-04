print('Hoàng Thanh Kiếm MSSV 235752021610003')
import sequential_search
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    dlist = []
    print(f"Nhập {n} phần tử vào danh sách:")
    for i in range(n):
        element = input(f"Phần tử {i+1}: ")
        dlist.append(element)
    item = input("Nhập phần tử cần tìm: ")
    result = sequential_search.Sequential_Search(dlist, item)
    if result != -1:
        print(f"Phần tử '{item}' được tìm thấy tại vị trí {result}.")
    else:
        print(f"Phần tử '{item}' không có trong danh sách.")

if __name__ == "__main__":
    main()
