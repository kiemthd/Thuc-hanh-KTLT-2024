print('Hoàng Thanh Kiếm MSSV 235752021610003')
# Viêt chương trinh tim so chia het cho 7 nhưng khong phai bôi so cua 5
# nằm trong đoạn 2000 và 3200(tính cả 2000 và 3200).
# gợi y sử dụng range(#begin,#end)

j=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))
