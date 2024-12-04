print('Hoàng Thanh Kiếm MSSV 235752021610003')
import re

def check_password(password):
  """Kiểm tra tính hợp lệ của một mật khẩu

  Args:
    password: Mật khẩu cần kiểm tra

  Returns:
    True nếu mật khẩu hợp lệ, False nếu không
  """

  # Biểu thức chính quy để kiểm tra các tiêu chí
  pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@^])[A-Za-z\d$#@^]{6,12}$"
  return re.match(pattern, password) is not None

def main():
  """Chương trình chính"""

  passwords = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
  password_list = passwords.split(',')

  valid_passwords = []
  for password in password_list:
    if check_password(password):
      valid_passwords.append(password) 


  print("Các mật khẩu hợp lệ:", ', '.join(valid_passwords))

if __name__ == "__main__":
  main()
