# Fixed points in math
# Y(R) = R(Y(R))
# Y(R) = (λx: R(x))(Y(R))
# Y(R) = (λx: R(x))(λx: R(x))  # repeat yourself
# Y(R) = (λx: R(x(x)))(λx: R(x(x)))  # maintain signature
# Y(R) = (λf: (λx: f(x(x)))(λx: f(x(x))))(R)  # pull out R
Y = λf: ((λx: f(x(x)))(λx:f(x(x))))


# THAT is the famous Y combinator
# Let's try to write our factorial with that
r = λf: (λx: 1 if x == 0 else x*f(x-1))
# fact = Y(r)


# Ah DAMN!. Python and it's eager evaluation
# We will introduce lazy evaluation using a wrapper function
Y = λf: ((λx: f(λz: x(x)(z)))\
         (λx: f(λz: x(x)(z))))

fact = Y(r)
print(fact(4))
print(fact(5))

# fun times! let's do fibonacci

r = λf: (λx: 1 if x <= 2 else f(x-2) + f(x - 1))
fib = Y(r)
print('fibo')
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
