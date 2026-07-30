D = int(input())
A = int(input())
N = int(input())
total_pagar = 0
diaria = 0


if N > 15:
    chegou = 15
else:
    chegou = N
    
diaria = ((chegou - 1)*A) + D
total_pagar = (31 - (N -1)) * diaria
print(total_pagar)


