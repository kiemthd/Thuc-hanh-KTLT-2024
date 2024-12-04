print('Hoàng Thanh Kiếm MSSV 235752021610003')
str=input("Enter a String:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] +=1
    else:
        dict[n] =1
print (dict)
