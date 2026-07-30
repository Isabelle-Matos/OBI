N =int(input())
R = int(input())
P = int(input())

prod = N
total = N
i = 0
while True:
    prod *= R
    total += prod
    i+= 1

    if total == P or total > P:
        break

print(i) 