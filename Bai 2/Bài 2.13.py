print('Hoàng Thanh Kiếm MSSV 235752021610003')
import math
print("giải hệ phương trình ax^2+bx+c=0")
a=float(input("nhập giá trị của a là:"))
b=float(input("nhập giá trị của b là:"))
c=float(input("nhập giá trị của c là:"))

if(a==0):
    if(b==0):
        if(c==0):
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print(f"Phương trình có nghiệm duy nhất: x = {x}")
else:
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b + math.sqrt(delta)) / (2*a)
        x2=(-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có nghiệm kép:x = {x}")
        print(f"x1={x1}")
        print(f"x2={x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép:x = {x}")
    else:
        print("Phương trình vô nghiệm")
