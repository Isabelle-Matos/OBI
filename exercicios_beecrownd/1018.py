div1= div2= div3= div4= div5= div6= div7= 0
x = int(input())
print(x)

if(x>=100):
    div1 = x/100
    x = x%100
if(x<100 and x>=50):
    div2= x/50
    x = x%50
if(x<50 and x>=20):
    div3= x/20
    x=x%20
if(x<20 and x>=10):
    div4=x/10
    x= x%10
if(x<10 and x>=5):
    div5=x/5
    x=x%5
if(x<5 and x>=2):
    div6= x/2
    x=x%2
if(x<2 and x>=1):
    div7=x/1
    x=x%1

print("%d nota(s) de R$ 100,0" % div1 );
print("%d nota(s) de R$ 50,00" %div2 )
print("%d nota(s) de R$ 20,00" %div3 )
print("%d nota(s) de R$ 10,00" %div4)
print("%d nota(s) de R$ 5,00" %div5 )
print("%d nota(s) de R$ 2,00" %div6 )
print("%d nota(s) de R$ 1,00" %div7 )
