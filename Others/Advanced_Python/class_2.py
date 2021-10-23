class Student():
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    # 객체 이름을 지정해주기 위한 메서드
    # 만약 __str__을 지정해주지 않았다면 print(객체) 출력 시 복잡한 형태로 도출.
    def __str__(self):
        return 'str {}'.format(self._name)
    
    # str메서드가 없을 때에는 print에서 repr메서드가 호출됨
    def __repr__(self):

        
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

# 따로 __dict__를 지정하지 않더라도 모든 클래스 객체들은 __dict__를 자동 생성함.
#print(studt1.__dict__)

# __str__에서 지정한 객체를 print해줌.
print(studt1) 