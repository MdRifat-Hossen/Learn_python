class person:
    def __init__(self,name,age):
        self.r=name
        self.a=age
    def prit(self):
        print(self.r,self.a)
#creat a child class
class student(person):
    def __init__(self, name, age,height,roll):
        super().__init__(name, age)
        self.h=height
        self.R=roll
        
    def same(self):
        print(self.r,self.a,self.h,self.R)
p=student('RIfat',78,25.3,220614)
p.same()
        