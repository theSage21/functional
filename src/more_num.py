zero = lambda x: lambda y: y
succ = lambda num: lambda f: lambda x: f(num(f)(x))

one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)


def incr(x):  # cheating. Just so that we can verify that numbers are actually working
    return x+1


print(zero(incr)(0) == 0)
print(one(incr)(0) == 1)
print(two(incr)(0) == 2)


# How do I go back? in order to subtract, I need to be able to go back to the
# predecessor of a number.

left = car = lambda x: lambda y: x
right = cdr = lambda x: lambda y: y
join = cons = lambda x: lambda y: lambda index: index(x)(y)

def ladder(pair):
    return join(succ(pair(left)))(pair(left))

def pred(num):
    return (num(ladder)(join(zero)(zero)))(right)

print(zero(incr)(0) == 0)
print(one(incr)(0) == 1)
print(two(incr)(0) == 2)
print(pred(three)(incr)(0) == 2)
print(pred(two)(incr)(0) == 1)
print(pred(one)(incr)(0) == 0)

sub = lambda x: lambda y: y(pred)(x)

print(sub(five)(two)(incr)(0) == 3)
