a = int(input())
b = int(input())
c = int(input())

P = a
D = 2*b
B = 3*c

soma = P + D + B
if soma >= 150:
    print("B")
elif soma >= 120:
    print("D")
elif soma >= 100:
    print("P")
elif soma < 100:
    print("N")