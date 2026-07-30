n = int(input())
count = 0

while count < n:
    x, y = [int(x) for x in input().split()]
    if y == 0:
        print("divisao impossivel")
    else:
        div = float(x/y)
        print(f"{div:.1f}")
    
    count+=1
