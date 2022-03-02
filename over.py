n=int(input("enter te limit"))
print("enter the values")
list=[]
for i in range(0,n):
    num=int(input())
    if(num>100):
        list.append("over")
        print(list)
    else:
        list.append(num)
