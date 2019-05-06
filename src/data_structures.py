from numbers import zero, incr, next_number

one = next_number(zero)
two = next_number(one)
three = next_number(two)
four = next_number(three)

def join(a):
    def fn(b):
        def index(x):
            return x(a)(b)
        return index
    return fn


list = join(three)(four)
# let's get the zeroth element. Since it's a function we'll use our increment
# trick to see things are working as expected

left = lambda x: lambda y: x
right = lambda x: lambda y: y

a = list(left)
b = list(right)
print(a(incr)(0) == 3)
print(b(incr)(0) == 4)
