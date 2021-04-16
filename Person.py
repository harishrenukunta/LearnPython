
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if(self.name == other.name and self.age == other.age):
            return True
        else:
            return False


harish = Person('Harish', 42)
radhika = Person('Radhika', 37)

harish2 = Person('Harish', 42)

if(harish.compare(radhika)):
    print(harish.name, ' and ', radhika.name, ' are same')
else:
    print(harish.name, ' and ', radhika.name, ' are not')

if(harish2.compare(harish)):
    print('harish and harish2 are same')
else:
    print('harish and harish2 are not same')
