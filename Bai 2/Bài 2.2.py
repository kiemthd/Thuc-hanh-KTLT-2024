print('Hoàng Thanh Kiếm MSSV 235752021610003')
import math;
# Nhập tọa độ của hai điểm
x1=int(input("Enter x1--->"))
y1=int(input("Enter y1--->"))

# Tính khoảng cách giữa hai điểm
x2=int(input("Enter x2--->"))
y2=int(input("Enter y2--->"))

# In kết quả
d1 = (x2 - x1) * (x2 - x1);
d2 = (y2 - y1) * (y2 - y1);
res = math.sqrt(d1+d2)
print("Distance between two points:",res);
