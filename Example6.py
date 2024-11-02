def example(a, b, x):
    for i in range(x + 1):
        c = (a**2)*i + b
        print(f"{a}x{a}x{i} + {b} = {c}")

a = int(input('a : '))
b = int(input('b : '))
x = int(input('x : '))

example(a,b,x)
