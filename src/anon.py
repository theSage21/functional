fact = λn: 1 if n == 0 else n*fact(n-1)
print(fact(3))

# we can't name the function! That's assignment, which was the whole point
# functional programming wanted to get rid of

print(
        (λf: λn: 1 if n == 0 else n * f(f)(n-1))\
        (λf: λn: 1 if n == 0 else n * f(f)(n-1))\
        (3)
      )

# ========== let's do it with pure lambda. no python cheating. 
# we will repeat what we did in the factorial function.
incr = λx: x + 1
succ = λn:λf:λx:f(n(f)(x))
left = true = λx:λy:x
right = false = λx:λy:y
iszero = λn:n(λf:false)(true)
mult = λa:λb:λx: a(b(x))
ladder = λp:join(succ(p(left)))(p(left))
pred = λn:(n(ladder)(join(zero)(zero)))(right)
join = λx:λy:λi: i(x)(y)

zero = λx:λy:y
one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)



lazy_true = λx:λy: x()
lazy_false = λx:λy: y()
iszero = λn: n(λf:lazy_false)(lazy_true)

fact = λn: iszero(n)\
        (λ: one)\
        (λ: (mult(n)(fact(pred(n)))))


# =============== let's check if our implementation works as expected
print('-'*100)
print(fact(zero)(incr)(0))
print(fact(one)(incr)(0))
print(fact(two)(incr)(0))
print(fact(three)(incr)(0))
print(fact(four)(incr)(0))

# We will assign it to a name so that we can test on multiple numbers.
fact = (λf: λn: iszero(n)(λ: one)(λ: (mult(n)(f(f)(pred(n))))))\
       (λf: λn: iszero(n)(λ: one)(λ: (mult(n)(f(f)(pred(n))))))

print('-'*10)
print(fact(zero)(incr)(0))
print(fact(one)(incr)(0))
print(fact(two)(incr)(0))
print(fact(three)(incr)(0))
print(fact(four)(incr)(0))
