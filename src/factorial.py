incr = λx: x + 1

# I'm going to use λ instead of lambda. Use `python lython.py file` to run this

zero = λx:λy:y
succ = λn:λf:λx:f(n(f)(x))

one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)

left = true = λx:λy:x
right = false = λx:λy:y

iszero = λn:n(λf:false)(true)
mult = λa:λb:λx: a(b(x))

join = λx:λy:λi: i(x)(y)
ladder = λp:join(succ(p(left)))(p(left))
pred = λn:(n(ladder)(join(zero)(zero)))(right)

# ================  python implementation

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4))
# ================ pure implementation
fact = λn: iszero(n)\
           (one)\
           (mult(n)(fact(pred(n))))
# print(fact(one)(incr)(0))
# Infinite recursion.  due to eager evaluation in python!
# Both branches are ALWAYS evaluated. so even if you reach fact(0), the other
# branch is ALSO evaluated and it loops back on itself from there

# one workaround is to wrap arguments in functions and call them when needed
lazy_true = λx:λy: x()
lazy_false = λx:λy: y()
iszero = λn: n(λf:lazy_false)(lazy_true)

fact = λn: iszero(n)\
        (λ: one)\
        (λ: (mult(n)(fact(pred(n)))))
print(fact(five)(incr)(0))
