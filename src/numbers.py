# How to have the 'concept' of numbers?

# Let counting happen by how many times you apply a function to an argument
def zero(x):  # don't call the function x
    def fn(y):
        return y  # apply zero times
    return fn

def one(x):
    def fn(y):
        return x(y)  # apply once
    return fn

def two(x):
    def fn(y):
        return x(x(y))  # apply twice
    return fn

def incr(x):  # cheating. Just so that we can verify that numbers are actually working
    return x+1


print(zero(incr)(0) == 0)
print(one(incr)(0) == 1)
print(two(incr)(0) == 2)


# It's tiring to write all the definitions. I need to GENERATE the next number


def next_number(num):
    def n_num(f):
        def fn(x):
            r = num(f)(x)  # apply as many times as given num
            return f(r)  # apply once more
        return fn
    return n_num

three = next_number(two)
four = next_number(three)
five = next_number(four)

print(three(incr)(0) == 3)
print(four(incr)(0) == 4)

# How to add???
# apply x times then apply y times.

def add(a):
    def fn(b):
        def result(x):
            return a(next_number)(b)(x)
        return result
    return fn


# all this def+return is too much typing
def add(a):
    def fn(b):
        return lambda x: a(next_number)(b)(x)
    return fn

def add(a):
    return lambda b: lambda x: a(next_number)(b)(x)

add = lambda a: lambda b: lambda x: a(next_number)(b)(x)

print(add(three)(four)(incr)(0) == 7)
print(add(three)(three)(incr)(0) == 6)
print(add(one)(two)(incr)(0) == 3)
print(add(zero)(two)(incr)(0) == 2)

def mult(a):
    def fn(b):
        def result(x):
            return a(b(x))
        return result
    return fn

def mult(a):
    def fn(b):
        return lambda x: a(b(x))
    return fn

def mult(a):
    return lambda b: lambda x: a(b(x))

mult = lambda a: lambda b: lambda x: a(b(x))
# mult = λa:λb:λx:a(b(x))
# mult = λabx:a(b(x))
# mult = λabx:abx
# mult = λabx.abx

# This is the notation that appears in most papers


print(mult(two)(three)(incr)(0) == 6)
print(mult(two)(two)(incr)(0) == 4)
print(mult(five)(three)(incr)(0) == 15)

def power(a):
    def fn(b):
        def result(x):
            return a(b)(x)
        return result
    return fn

power = lambda a: lambda b: lambda x: b(a)(x)

print(power(two)(three)(incr)(0) == 8)
print(power(five)(two)(incr)(0) == 25)
print(power(five)(zero)(incr)(0) == 1)
print(power(five)(one)(incr)(0) == 5)
