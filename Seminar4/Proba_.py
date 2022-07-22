


def kalk(f, x,y):
    print(f(x,y))
kalk(lambda a, b: a * b,4,5)

def kalk(f, x,y):
    return f(x,y)
print(f'аля ',kalk(lambda a, b: a * b,4,5))

def kalk(f, x,y):
    return f(x,y)

print(f'а3ля ',kalk(lambda a, b: a * b,4,5))