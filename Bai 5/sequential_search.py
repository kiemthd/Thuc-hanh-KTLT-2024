# sequential_search.py

def Sequential_Search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính trong danh sách dlist để tìm phần tử item.
    Trả về chỉ số của phần tử nếu tìm thấy, hoặc -1 nếu không tìm thấy.
    """
    for index in range(len(dlist)):
        if dlist[index] == item:
            return index  # Trả về chỉ số của phần tử tìm thấy
    return -1  # Trả về -1 nếu không tìm thấy phần tử
