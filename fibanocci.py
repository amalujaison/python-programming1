n=int(input("enter the no of series"))
a=0
b=1
count=0
while count<=n:
    print(a)
    f=a+b
    a=b
    b=f
    count=count+1