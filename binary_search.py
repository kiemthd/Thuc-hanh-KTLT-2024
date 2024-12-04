# binary_search.py
def binary_search(sorted_list, value):
    left, right = 0, len(sorted_list) - 1  # Khởi tạo các chỉ số trái và phải
    while left <= right:  # Khi nào vẫn còn khoảng cách giữa trái và phải
        mid = (left + right) // 2  # Tính chỉ số giữa (mid)
        
        # Kiểm tra phần tử ở giữa
        if sorted_list[mid] == value:  # Nếu phần tử ở giữa bằng giá trị cần tìm
            return mid  # Trả về chỉ số của phần tử tìm thấy
        elif sorted_list[mid] < value:  # Nếu phần tử giữa nhỏ hơn giá trị cần tìm
            left = mid + 1  # Thay đổi trái để tìm trong nửa sau
        else:  # Nếu phần tử giữa lớn hơn giá trị cần tìm
            right = mid - 1  # Thay đổi phải để tìm trong nửa trước
    
    return -1  # Nếu không tìm thấy giá trị, trả về -1
