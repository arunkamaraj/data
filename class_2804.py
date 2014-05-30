class GrandParent:
	var1=200
	def __init__(self):
		print "GrandParent Contructor"
	def gfun(self):
		print "GrandParent function"
class Parent:
	__var1=100 #stongly private
#	_var=100 # private
	def __init__(self):
		print 'parent construtor'
	def pfun(self):
		print 'parent function'
class Child(GrandParent,Parent):                            
	def __init__(self):
		Parent.__init__(self) # calling the parent class constructor
		print 'Child construcor'
	def cfun(self):
		print "child functio"
obj=Child()
obj.gfun()
obj.pfun()
obj.cfun()
print obj.var1,obj.var1
print obj._Parent__var1 # strongly private 
#print obj._var private 
sub=issubclass(GrandParent,Parent)
ins=isinstance(obj,GrandParent)
print "is subclass ?",sub
print "is instance ?",ins
