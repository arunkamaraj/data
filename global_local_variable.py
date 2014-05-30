def fun1(a):
            print 'a:', a
            a= 33;
            print 'local a: ', a
a = 100
fun1(a)
print 'a outside fun1:', a
def fun2():
           global b
           print 'b: ', b
           b = 33
           print 'global b:', b
b =100
fun2()
print 'b outside fun2', b
