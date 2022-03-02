class rectangle:
    def _init_(self,l,b):
        self.len=l
        self.br=b
    def area(self):
        area1=self.len*self.br
        return area1
    def perimeter(self):
        perimeter1=2*(self.len+self.br)
        return perimeter1
    def comp(self,obj):
        if(self.area()>obj.area()):
            print("GREATER")
        else:
            print("LESSER")


rect1=rectangle(10,5)
rect1.perimeter()
obj=rectangle(20,2)
obj.perimeter()
rect1.comp(obj)
