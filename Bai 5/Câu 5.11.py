print('Hoàng Thanh Kiếm MSSV 235752021610003')
import numpy as np
data_type = np.dtype([('name', 'U50'), ('height', 'f4'), ('class', 'U20')])
students = np.array([('Đào Quang Huy', 180, '12A'),
                     ('Ngô Mạnh Nguyên', 160, '11B'),
                     ('Nguyễn Hữu Kiều', 165, '12A'),
                     ('Nguyễn Thái Huy', 175, '11B'),
                     ('Lê Văn Hoàng', 168, '12B')],
                    dtype=data_type)
sorted_students = np.sort(students, order=['class', 'height'])
for student in sorted_students:
    print(f"Tên: {student['name']}, Chiều cao: {student['height']} cm, Lớp: {student['class']}")
