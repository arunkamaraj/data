class A(object):
	pass
class B(A):
	pass
class C(B):
	pass

#obj=C()
print C.__mro__

