zero = lambda x:lambda y:y
one = lambda x:lambda y: x(y)
two = lambda x:lambda y: x(x(y))
three = lambda x:lambda y: x(x(x(y)))
true = lambda x: lambda y: x
false = lambda x: lambda y: y
iszero = lambda num: num(lambda fn: false)(true)

def incr(x):
    return x + 1

print(iszero(one)('true')('false'))
print(iszero(zero)('true')('false'))
print(iszero(two)('true')('false'))
print(iszero(three)('true')('false'))
