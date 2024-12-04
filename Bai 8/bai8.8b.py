import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lựa chọn thông tin")

# Tạo biến lưu giá trị RadioButton
v = tk.IntVar()
v.set(1)  # Giá trị mặc định

# Hàm hiển thị thông tin RadioButton đang được chọn
def show_choice():
    tk.Label(root, text=f"Bạn đã chọn: {v.get()}", font=("Arial", 12), fg="blue").grid(row=4, column=0, columnspan=2, pady=10)

# Tiêu đề
tk.Label(root, text="Chọn một số:", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

# Tạo các RadioButton
tk.Radiobutton(root, text="Số 1", variable=v, value=1, font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=20)
tk.Radiobutton(root, text="Số 2", variable=v, value=2, font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=20)
tk.Radiobutton(root, text="Số 3", variable=v, value=3, font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=20)

# Nút "Click Me"
tk.Button(root, text="Click Me", command=show_choice, font=("Arial", 12), bg="lightblue").grid(row=1, column=1, rowspan=3, padx=10, pady=5)

# Vòng lặp chính
root.mainloop()
