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

    # Class Method
    # cls는 Student라는 class 그 자체이기 때문에, cls에 객체들을 넣어도 된다.
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    # --> Class와 밀접한 일을 하는 Method에 대해, 
    # self라는 인자도 받지 않고 cls라는 인자도 받지 않는
    # inst라는 변수로 누구나 공통으로 사용 가능한 Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. Not a scholarship recipient.'
    
    def __str__(self):
        return 'Student Info -> name: {} grade: {} email: {}'.format(self.full_name(), self._grade, self._email)

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

# 클래스 메소드 인스턴스 생성하기
student_3 = Student.student_const(3, 'Park', 'Minji', 'Student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'Student4@naver.com', '4', 600, 4.1)

# 전체 정보
#print(student_3.detail_info())
#print(student_4.detail_info())
#print()

# 학생 학비 변경 확인
#print(student_3._tuition)
#print(student_4._tuition)
#print()

# 장학금 혜택 여부(스테이틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'

# 장학금 혜택 여부(스테이틱 메소드 사용)
print('Static : ', Student.is_scholarship_st(student_1))
print('Static : ', Student.is_scholarship_st(student_2))
print('Static : ', Student.is_scholarship_st(student_3))
print('Static : ', Student.is_scholarship_st(student_4))
print()

# 더불어, 각 self 객체들에 대해서도 staticmethod를 사용할 수 있다.
print('Static : ', student_1.is_scholarship_st(student_1))
print('Static : ', student_2.is_scholarship_st(student_2))
print('Static : ', student_3.is_scholarship_st(student_3))
print('Static : ', student_4.is_scholarship_st(student_4))