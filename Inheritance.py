class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature1 is working')

    def feature2(self):
        print('Feature2-A is working')

class B(A):
    def __init__(self):
        super().__init__()
        print('Init B printing')

    def feature2(self):
        print('Feature2-B is working')

    def feature4(self):
        print('Feature4 is working')

b1 = B()
b1.feature2()