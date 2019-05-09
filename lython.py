import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-v', '--verbose', default=False, action='store_true')
args = parser.parse_args()

with open(args.file, 'r') as fl:
    lines = fl.readlines()
    final = ''
    for line in lines:
        if line.count('λ') == 1 and line.count('.') == 1:
            pre, post = line.split('λ')
            var, eqn = post.split('.')
            line = pre + ' '.join([f'lambda {v}: ' for v in var]) + eqn
        elif line.count('λ') >= 1 and line.count(':') >= 1:
            line = line.replace('λ', 'lambda ')
        final += line
    if args.verbose:
        print('-'*100)
        print(final)
        print('-'*100)
    exec(final)
