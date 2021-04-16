
def name(na):
    return na

def smart_name(func):
    def inner(name):
        name = name + ' Renukunta'
        return func(name)
    return inner

name = smart_name(name)
print('Full name:', name('Harish'))