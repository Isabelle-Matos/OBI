n = int( input())
count = 0
in_num = 0
out_num = 0
# intervalo [10,20]

while count < n:
    a = int(input())
    if a >= 10 and a <=20:
        in_num+=1
    else:
        out_num+=1
    count+=1
print("%d in" %in_num)
print("%d out" %out_num)