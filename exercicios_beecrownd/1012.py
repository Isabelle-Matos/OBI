pi = 3.14159
area_tri = 0
area_cir = 0
area_trap = 0
area_quad = 0
area_ret = 0

x, y, z = [float(x) for x in input().split()]
area_tri = (x*z)/2
area_cir = pi*(z*z)
area_trap = ((x+y)*z)/2
area_quad = y*y
area_ret = x*y

print(f"TRIANGULO: {area_tri:.3f}");
print(f"CIRCULO: {area_cir:.3f}");
print(f"TRAPEZIO: {area_trap:.3f}");
print(f"QUADRADO: {area_quad:.3f}");
print(f"RETANGULO: {area_ret:.3f}");


