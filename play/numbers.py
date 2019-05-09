# first let's define zero and +1, -1
zero = λxy.y
succ = λnfx.f(n(f)(x))

tuple = λabi.i(a)(b)
negative = left = true = λab.a
positive = right = false = λab.b
iszero = λn:n(λf:false)(true)
ladder = λp.tuple(succ(p(left)))(p(left))
pred = λn.n(ladder)(tuple(zero)(zero))(right)

# now let's say a number is actually a tuple of (sign, magnitude)
# zero is considered positive
_zero = tuple(positive)(zero)
_succ = λn.(tuple
            (n(left)
                (iszero(pred(n(right)))
                    (positive)
                    (negative)
                )
                (positive)
            )
            (n(left)
                (pred(n(right)))
                (succ(n(right)))
            )
           )
_pred = λn.(tuple
            (n(left)
                (negative)
                (
                    iszero(n(right))
                    (negative)
                    (n(left))
                )
            )
            (n(left)
                (succ(n(right)))
                (
                    iszero(n(right))
                        (succ(n(right)))
                        (pred(n(right)))
                )
            )
           )



def show(_n):
    "A helper function to visualize a signed integer"
    def inc(x):
        return x + 1
    sign = '?'
    sign = '+' if _n(left) == positive else sign
    sign = '-' if _n(left) == negative else sign
    print(sign, _n(right)(inc)(0))


# let's say we have -3 as a starting point.
# Can we count up to 3 and come back?

x = zero
mag = 3
for _ in range(mag):
    x = succ(x)
x = tuple(negative)(x)
# ============== start counting up
for _ in range(mag*2+1):
    show(x)
    x = _succ(x)
print('-'*10)
# -------------- start counting back
for _ in range(mag*2+1):
    x = _pred(x)
    show(x)
# ====================== awesome! we have signed integers


# how would we do addition?
# old addition was λab.a(succ)(b)
