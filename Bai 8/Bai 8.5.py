import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chọn ngôn ngữ lập trình yêu thích")

# Tạo biến lưu giá trị của RadioButton
v = tk.IntVar()
v.set(1)  # Giá trị mặc định ban đầu

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm xử lý khi chọn một RadioButton
def ShowChoice():
    print(f"Ngôn ngữ bạn chọn là: {languages[v.get() - 1][0]}")

# Tiêu đề của ứng dụng
tk.Label(
    root,
    text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
    justify=tk.LEFT,
    padx=20
).pack()

# Tạo các RadioButton
for language, val in languages:
    tk.Radiobutton(
        root,
        text=language,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val
    ).pack(anchor=tk.W)

# Vòng lặp chính
root.mainloop()
