class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._number)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._number)
    

student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88})
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 77, 'score2': 92})
student3 = Student('Park', 3, 4, {'gender': 'Male', 'score1': 99, 'score2': 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)