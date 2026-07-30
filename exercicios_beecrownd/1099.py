n = int(input())
impares_soma = 0
count = 0

while count<n:
    a, b= [int(x) for x in input().split()]
    if a < b:
        for x in range(a+1,b):
            if x%2 !=0:
                impares_soma+=x
        print(impares_soma)
    else:
        for x in range(b+1,a):
            if x%2!=0:
                impares_soma+=x
        print(impares_soma)
    impares_soma = 0
    count+=1

