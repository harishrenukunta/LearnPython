
class Computer:
    def __init__(self, cpu, ram, hdb):
        self.cpu = cpu
        self.ram = ram
        self.hdb = hdb

    def showConfig(self):
        print('CPU:', self.cpu, 'RAM:', self.ram, 'HDB:', self.hdb)

comp1 = Computer('i5', '16gb', '1TB')
comp2 = Computer('i7', '32gb', '512GB')
comp3 = Computer('AMD', '16gb', '256GB')

comp1.showConfig()
comp2.showConfig()
comp3.showConfig()