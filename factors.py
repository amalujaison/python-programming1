def factors(x):
    print("the factors are")
    for i in range(1,x+1):
        if(x%i==0):
            print(i)
num=int(input("enter the value"))
factors(num)
