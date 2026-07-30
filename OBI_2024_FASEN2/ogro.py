def verifica(e, d):
    if e > d:
        return e+d
    else:
        return 2*(d-e)

e = int(input())
d = int(input())

resposta =  verifica(e,d)

print(resposta)