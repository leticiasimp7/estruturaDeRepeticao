x=1
y=0
z=0
n1=0
while (x<=10):
    n=int(input("Digite um número: "))
    n1=n1+n

    if n%2==0:
        y=y+1

    else:
        z=z+1
    x=x+1

    print(z,y,n1)
          
