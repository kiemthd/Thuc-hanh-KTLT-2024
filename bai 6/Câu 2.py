print('Hoàng Thanh Kiếm MSSV 235752021610003')
class Hinhchunhat:
  def __init__(self, chieudai, chieurong):
    self.chieudai = chieudai
    self.chieurong = chieurong
  def tinh_dien_tich(self):
    return self.chieudai * self.chieurong
hinh_chu_nhat = Hinhchunhat(16, 8)
dien_tich = hinh_chu_nhat.tinh_dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich)
