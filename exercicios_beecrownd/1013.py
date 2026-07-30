x, y, z = [int(x) for x in input().split()]
maior = (x+y+abs(x-y))/2
maior = (maior+z+abs(maior -z))/2
print("%d eh o maior" %maior);
