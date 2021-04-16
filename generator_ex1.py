
def topten():
    yield 3
    yield 100
    yield 60

def toptensqrs():
    n = 1
    while n <= 10:
        sqr = n * n
        yield sqr
        n += 1

values = topten()
for i in values:
    print(i)

values = toptensqrs()
for i in values:
    print(i)