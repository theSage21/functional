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
        def fn(y):
            r = num(f)(y)
            return f(r)
        return fn
    return n_num

three = next_number(two)
four = next_number(three)

three(show)(1)
print('-'*10)
four(show)(1)
