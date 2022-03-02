list=(input("enter the string"))
char=list[0]
list=list.replace(char,'$')
list=char+list[1:]
print(list)

