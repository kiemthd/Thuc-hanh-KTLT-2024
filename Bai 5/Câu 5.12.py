print('Hoàng Thanh Kiếm MSSV 235752021610003')
import numpy as np
student_ids = np.array([101, 102, 103, 104, 105])
heights = np.array([170, 160, 165, 175, 168])
sorted_indices = np.lexsort((heights,))  
print("Chỉ số sắp xếp (theo chiều cao):", sorted_indices)
sorted_student_ids = student_ids[sorted_indices]
sorted_heights = heights[sorted_indices]
print("Dữ liệu sau khi sắp xếp:")
for id, height in zip(sorted_student_ids, sorted_heights):
    print(f"ID: {id}, Chiều cao: {height} cm")
