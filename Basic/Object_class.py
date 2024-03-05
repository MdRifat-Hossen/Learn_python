# #class 
# class rifat:
#     name="rifatHossen"
#     age=67

# #object
# p1=rifat()
# print(p1.age,p1.name)
# --init(self)__construction er moton kaj kore
class person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
p=person("RIfat HOssen",23)
print(p.age,p.name) 
q=person("Hasan",78)
print(q)

#__str__() return the value
class person :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def __str__(self) :
        return f"{self.name}{self.age}"
    def prin(self):
        print(self.name,self.age)
p=person("Habib",787)
p.age=56
p.prin()