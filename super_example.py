class A(object):
	def data(self):
		print "data of A"
class B(A):
	def data(self):
		print "data of B"
class D(A):
	def data(self):
		print "data of D"

class C(D,B):
	def data(self):
		print "data of C"
		super(C,self).data() # it just calling base class 
		B.data(self) # amazing example 

obj=C()
obj.data()
print C.__mro__
