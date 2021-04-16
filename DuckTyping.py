
class PyCharm:
    def execute(self):
        print('PyCharm editor')
        print("Compiling")
        print('Executing')


class VsCode:
    def execute(self):
        print('Vscode editor')
        print('Code review')
        print('Spell check')
        print('Compiling')
        print('Executing')
        print('Packaging')

class Laptop:
    def __init__(self, ide):
        ide.execute()


pyCharmIDE = PyCharm()
vsCodeIDE = VsCode()

lap1 = Laptop(pyCharmIDE)
lap2 = Laptop(vsCodeIDE)
