print('Hoàng Thanh Kiếm MSSV 235752021610003')
import numpy as np
dt = np.dtype([('Tên', 'U50'), ('Chiều cao', 'f4'), ('Lớp', 'U20')])
data = np.array([('Đào Quang Huy', 1.75, '12A1'),
                 ('Ngô Mạnh Nguyên', 1.60, '12B1'),
                 ('Đào Mạnh Nguyên', 1.80, '12A2'),
                 ('Ngô Quang Huy', 1.65, '12C1')], dtype=dt)
sorted_data = np.sort(data, order='Chiều cao')
print(sorted_data)
