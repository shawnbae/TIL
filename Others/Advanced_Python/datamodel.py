# Python의 중요한 핵심 Framework
# 시퀀스 (Sequence), 반복 (Iterator), 함수 (Function), 클래스 (Class)

# 일반적인 튜플 사용

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

line_leng_1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

#print(line_leng_1)

# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언 후 클래스와 같이 객체를 할당하여 사용할 수 있다.
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_leng_2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

print(line_leng_2)

# 네임드 튜플 선언 방식들
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False, 중복된 이름이 있을 때 알아서 바꿔 key값을 넣어줌.

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

print("Point들 출력해보기: ", p1, p2, p3, p4)