# def hello1():
#     print("Hello I love to code python")
# def hello2():
#     return "Hello"
# hello1()
# print(hello2())
def add(x,y):
    print("add")
    return (x+y)
def minus(x,y):
    print("minus")
    return (x-y)
def mul(x,y):
    print("mul")
    return (x*y)
def vag(x,y):
    print("vag")
    return (x/y)
def main():
    print("main menu...")
    print("1.add")
    print("2.minus")
    print("3.mul")
    print("4.vag")
    cha=int(input("Entehr number: "))
    return cha
def cal():
    ch=main()
    n=int(input("Num1:"))
    n1=int(input("Num2: "))
    
    if ch==1:
        result=add(n,n1)
    elif ch==2:
        result=minus(n,n1)
    elif ch==3:
        result=mul(n,n1)
    elif ch==4:
        result=vag(n,n1)
    print("result = ",result)

cal()   
    