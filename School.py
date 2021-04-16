
class School:

    def __init__(self, name, noOfStudents, add, pc):
        self.name = name
        self.no_of_students = noOfStudents
        self.address = self.Address(add, pc)

    def show(self):
        print('Name:', self.name, ' Students count:', self.no_of_students)

    class Address:
        def __init__(self, addressLine1, postcode):
            self.addressLine1 = addressLine1
            self.postcode = postcode

        def show(self):
            print('Addr:', self.addressLine1, self.postcode )

school1 = School('Jyothi Bala Mandir', 3000, 'Ramnagar', '5000013')
school1.show()
school1.address.show()