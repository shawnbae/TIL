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



