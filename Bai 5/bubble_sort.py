# bubble_sort.py

def bubbleSort(nlist):
    """
    Hàm sắp xếp nổi bọt (Bubble Sort) sắp xếp một danh sách theo thứ tự tăng dần.
    :param nlist: Danh sách các số cần sắp xếp
    :return: Danh sách đã sắp xếp
    """
    n = len(nlist)
    
    # Duyệt qua toàn bộ danh sách
    for i in range(n):
        # Duyệt qua các phần tử chưa sắp xếp
        for j in range(0, n-i-1):
            # So sánh hai phần tử liền kề
            if nlist[j] > nlist[j+1]:
                # Hoán đổi nếu phần tử tại j lớn hơn phần tử tại j+1
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    
    return nlist
