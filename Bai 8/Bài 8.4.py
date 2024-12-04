from tkinter import *

# Tạo cửa sổ chính
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')  # Đặt kích thước cửa sổ

# Tạo nhãn (Label)
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm xử lý sự kiện khi bấm nút
def clicked():
    lbl.configure(text="Button was clicked !!")

# Tạo nút (Button)
btn = Button(window, text="Click Me", bg="blue", fg="white", command=clicked)
btn.grid(column=1, row=0)

# Vòng lặp chính để hiển thị cửa sổ
window.mainloop()
