room = input()
if room == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    S = ((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)) ** 0.5
    print(S)
elif room == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a*b
    print(S)
else:
    a = int(input())
    S = 3.14*a**2
    print(S)