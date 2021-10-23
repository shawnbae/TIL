class Student():
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

# 따로 __dict__를 지정하지 않더라도 모든 클래스 객체들은 __dict__를 자동 생성함.
print(studt1.__dict__)