print('Hoàng Thanh Kiếm MSSV 235752021610003')
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân")

# Tạo các nhãn và giá trị thông tin cá nhân
tk.Label(root, text="Họ và tên:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Ngô Mạnh Nguyên", font=("Arial", 12)).grid(row=0, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Ngày sinh:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="06/10/2005", font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="MSSV:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="235752021610058", font=("Arial", 12)).grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(root, text="Ngành học:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="KTDK&TDH", font=("Arial", 12)).grid(row=3, column=1, sticky="w", padx=10, pady=5)

# Vòng lặp chính
root.mainloop()
