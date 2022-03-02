start=int(input("enter the start year"))
end=int(input("enter the end year"))
for year in range(start,end):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print("the leap year is:",year)