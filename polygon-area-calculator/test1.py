from shape_calculator import *  # Rectangle, Square

print('W: 10 | H: 2')
rect1 = Rectangle(10, 2)
print(rect1)
print(rect1.get_perimeter())
print(rect1.get_area())
print(rect1.get_diagonal())
print(rect1.get_picture())
print('W: 10 | H: 4')
rect1.set_height(4)
print(rect1)
print(rect1.get_perimeter())
print(rect1.get_area())
print(rect1.get_diagonal())
print(rect1.get_picture())
print('W: 17 | H: 4')
rect1.set_width(17)
print(rect1)
print(rect1.get_perimeter())
print(rect1.get_area())
print(rect1.get_diagonal())
print(rect1.get_picture())

rect2 = Rectangle(11, 4)
rect3 = Rectangle(4, 4)

print(rect2.get_amount_inside(rect3))

sq1 = Square(4)
rect5 = Rectangle(3, 6)

print(sq1.get_amount_inside(rect5))
print(rect5.get_amount_inside(sq1))
