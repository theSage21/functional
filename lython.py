import sys

with open(sys.argv[1], 'r') as fl:
    text = fl.read()
    text = text.replace('λ', 'lambda ')
    exec(text)
