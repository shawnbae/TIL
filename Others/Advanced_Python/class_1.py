class Student():
    """
    Student Class
    Author : Bae
    Date : 2021.10.23
    Description : Advance Class 직접 짜기
    """
    # 클래스 변수
    student_count = 0

    # 초기화 함수
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1


    # 객체 이름을 지정해주기 위한 메서드
    # 만약 __str__을 지정해주지 않았다면 print(객체) 출력 시 복잡한 형태로 도출.
    def __str__(self):
        return 'str {}'.format(self._name)
    
    # str메서드가 없을 때에는 print에서 repr메서드가 호출됨
    def __repr__(self):
        return 'repr {}'.format(self._name)

    # self 객체의 고유값을 보고싶을 땐 id함수를 사용할 수 있다.
    def detail_info(self):
        print("Current Id : {}".format(id(self)))
        print("Student Detail Info : {} {} {}".format(self._name, self._email, self._details))

    # 객체를 지우는 메서드
    def __del__(self):
        Student.student_count -= 1

# 객체 지정하기
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

# __str__에서 지정한 객체를 print해줌.
# __str__이 존재하지 않는다면 __repr__을 print함
# print(repr(studt1))과 같이 repr을 지정하여 print할 수도 있음.
#print(studt1)

# 메모리에 저장된 id값 확인하기
#print(id(studt1))
#print(id(studt2))

# dir함수 및 속성값(dict) 확인하기
# 따로 __dict__를 지정하지 않더라도 모든 클래스 객체들은 __dict__를 자동 생성함.
#print(dir(studt1)) # 인스턴스들은 보여주나 그에 대한 속성값까지 알려주지는 않음.
#print(dir(studt2))
#print(studt1.__dict__) # 인스턴스들의 속성값까지 보고 싶을 때

# Doctring: Class의 주석 보기
#print(Student.__doc__)

# detail_info 메서드
#print(studt1.detail_info()) 
#print(Student.detail_info(studt1)) # 클래스 그 자체로 출력하기

# 클래스 출력하기
#print(studt1.__class__)

# 인스턴스 변수
# 직접 접근하는 방식은 Python과 맞지 않는다.
#print(studt1._name, studt2._name)
#print(studt1._email, studt2._email)
#print(Student.student_count) # 클래스 변수 접근

# 공유 확인
# 인스턴스 네임스페이스에 존재하지 않을 때엔 상위에서 검색함.
# 즉, 동일한 이름으로 변수를 생성할 수 있음 (인스턴스 검색 -> 상위 (클래스 변수, 부모 클래스 변수 등))
#print(Student.__dict__)
#print(studt1.__dict__)

#del studt2 # 학생 정보 지우기
#print(studt1.student_count)
#print(Student.student_count)