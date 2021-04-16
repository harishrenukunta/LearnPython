
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def total(self):
        return self.m1 + self.m2

    def __str__(self):
        return 'm1:{} m2:{}'.format(str(self.m1), str(self.m2))

    def __gt__(self, other):
        if self.total() > other.total():
            return True
        else:
            return False

harish = Student(78, 75)
print('Harish total score:', harish.total())
tanvi = Student(75, 85)
print('Tanvi total score:{}'.format(tanvi.total()))

print('Harish marks:', harish)
print('Tanvi marks:', tanvi)

print('Tanvi scored more marks than Harish:', tanvi > harish)
