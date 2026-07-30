f = float(input())
faixa1, faixa2, faixa3 = 0, 0, 0

if f > 0 and f <= 2000.00:
    print("Isento")
elif f > 2000.00 and f <= 3000.00:
    faixa1 = f -2000.00
    desc = faixa1*0.08
    print(f"R$ {desc:.2f}")
elif f > 3000.00 and f <= 4500.00:
    faixa1 = 1000.00
    faixa2 = f - 3000.00
    desc = (faixa2*0.18) + (faixa1*0.08)
    print(f"R$ {desc:.2f}")
else:
    faixa3= f-4500.0
    faixa2= 1500.0
    faixa1 = 1000.0
    desc = (faixa3*0.28) + (faixa2*0.18) + (faixa1*0.08)
    print(f"R$ {desc:.2f}")