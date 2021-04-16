
class Student:

    school_name = 'Jyothi Bala Mandir'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def info():
        print('This is a static method....in Student class')

s1 = Student(98, 92, 93)
s2 = Student(82, 81, 80)
print('Avg s1:', s1.avg())
print('Avg s2:', s2.avg())
print('Access class level variable:name:', Student.get_school_name())
print('Info:', Student.info())