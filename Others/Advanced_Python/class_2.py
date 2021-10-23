class Student(object):
    """
    Student Class 정보
    Author : Me
    Date : 2021.10.23
    Description : Class, Static, Instance Method
    """

    # Class Variable
    tuition_per = 1.0
    
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa
    
    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)
    
    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> id : {}, fee : {}'.format(self._id, self._tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    # Class Method
    # self변수가 한 객체에 대한 변수라면, cls는 클래스 변수로 공용 변수이다.
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("Please Enter 1 or more")
            return
        cls.tuition_per = per
        print("Suceed! tuition increased!")











# 학생 인스턴스    
student_1 = Student(1, 'Kim', 'Sarang', 'Student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'Student2@daum.net', '2', 500, 4.3)

# 기본 정보
#print(student_1)
#print(student_2)
#print()

# 전체 정보
#print(student_1.detail_info())
#print(student_2.detail_info())
#print()

# 학비 정보 (학비 인상 전)
#print(student_1.get_fee())
#print(student_2.get_fee())
#print()

# 학비 인상 (클래스 메소드 미사용, 직접 접근 방식)
#Student.tuition_per = 1.2

# 학비 정보 (인상 후)
#print(student_1.get_fee_culc())
#print(student_2.get_fee_culc())
#print()

# 학비 인상을 Class Method를 사용하여 실행
Student.raise_fee(1.5)












