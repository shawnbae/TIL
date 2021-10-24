# 매직 메서드 / 스페셜 메서드

# 덧셈을 하는 순간, __add__라는 매직 메서드가 내부적으로 작동하는 방식이다.
n = 100

# 다양한 매직메서드 예시
#print("n + 200: ", n + 200)
#print("n + 200(magicmethod): ", n.__add__(200))
#print("__doc__: ", n.__doc__)
#print("__bool__: ", n.__bool__(), bool(n))
#print("__mul__: ", n * 100, n.__mul__(100))

# Student Class 정의
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height
    
    # 학생의 객체 정보를 정의해주는 메서드 정의
    def __str__(self):
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    # 학생의 키를 비교하기 위한 greater equal 매직 메서드 정의
    def __ge__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    # 학생의 키를 비교하기 위한 less equal 매직 메서드 정의
    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    # 학생의 키의 차이를 반환하는 매직 메서드 정의
    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._height - x._height
        
# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 매직메소드 출력
print("키 비교하기: ", s1 >= s2)
print("키의 차이: ", s1-s2)