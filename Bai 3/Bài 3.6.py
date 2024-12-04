print('Hoàng Thanh Kiếm MSSV 235752021610003')
def get_sum(*num):
    tmp=0
    # duyệt các tham số
    for i in num:
        tmp +=i
    return tmp
result = get_sum(1,2,3,4,5)
print(result)
