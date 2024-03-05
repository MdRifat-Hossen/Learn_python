def fun():
    x=20
    def fun1():
        global x
        x=25
    print("Beforglobal",x)
    print("calling funtion2")
    fun1()
    print("fun1:",x)
fun()
print("main valu of x", x)    

