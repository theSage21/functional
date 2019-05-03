def true(x):
    def f(y):
        return x
    return f

def false(x):
    def f(y):
        return y
    return f

def NOT(x):
    return x(false)(true)

def AND(x):
    def f(y):
        return x(y(true)(false))(false)
    return f

def OR(x):
    def f(y):
        return x(true)(y(true)(false))
    return f

print(NOT(true))
print(NOT(false))

print(AND(true)(false), 'f')
print(AND(false)(true), 'f')
print(AND(true)(true), 't')
print(AND(false)(false), 'f')

print(OR(true)(false), 't')
print(OR(false)(true), 't')
print(OR(true)(true), 't')
print(OR(false)(false), 'f')
