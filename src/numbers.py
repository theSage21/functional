def zero(x):
    def fn(y):
        return y
    return fn

def one(x):
    def fn(y):
        return x(y)
    return fn

def two(x):
    def fn(y):
        return x(x(y))
    return fn

def show(x):
    print(x)
    return x


zero(show)(1)  # nothing
print('-'*10)
one(show)(1)  # 1
print('-'*10)
two(show)(1)  # 1 1
print('-'*10)


def next_number(num):
    def n_num(f):
        def fn(x):
            r = num(f)(x)
            return f(r)
        return fn
    return n_num

def incr(x):
    return x + 1

three = next_number(two)
four = next_number(three)
five = next_number(four)

print(three(incr)(0))
print('-'*10)
print(four(incr)(0))


def mult(a):
    def fn(b):
        def result(x):
            return a(b(x))
        return result
    return fn
print('--- mult')
print(mult(three)(four)(incr)(0))
print(mult(three)(three)(incr)(0))
print(mult(two)(five)(incr)(0))


def add(a):
    def fn(b):
        def result(x):
            return a(next_number)(b)(x)
        return result
    return fn

print('--- add')
print(add(three)(four)(incr)(0))
print(add(three)(three)(incr)(0))
print(add(one)(two)(incr)(0))
print(add(zero)(two)(incr)(0))
