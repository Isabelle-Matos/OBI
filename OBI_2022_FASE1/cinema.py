a = int(input())
b = int(input())
valor_total = 0

if a <= 17:
    valor_total += 15
elif a >= 18 and a <= 59:
    valor_total += 30
elif a >= 60:
    valor_total+= 20

if b <= 17:
    valor_total += 15
elif b >= 18 and b <= 59:
    valor_total += 30
elif b >= 60:
    valor_total+= 20

print(valor_total)