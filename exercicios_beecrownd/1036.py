import math
a, b, c = [float(x) for x in input().split()]

bask = pow(b,2) -(4*a*c)

if(bask<0 or a==0):
   print("Impossivel calcular")
else:
   x1 = ((-b + math.sqrt(bask))/(2*a))
   x2 = ((-b - math.sqrt(bask))/(2*a))
   print(f"R1 = {x1:.5f}")
   print(f"R2 = {x2:.5f}")
 
