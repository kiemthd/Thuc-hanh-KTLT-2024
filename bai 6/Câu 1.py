print('Hoàng Thanh Kiếm MSSV 235752021610003')
class Circle(object):
    def __init__(self, r):
        """Constructor nhận vào bán kính của hình tròn."""
        self.radius = r
    def area(self):
        """Method tính diện tích hình tròn."""
        return self.radius**2 * 3.14
aCircle = Circle(8)
print(aCircle.area())
