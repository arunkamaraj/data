class B():
	def __init__(self,x):
		self.x=x
	def __iter__(self):
		return self
	def next(self):
		if self.x>0:
			self.x-=1
			return self.x
		else:
			raise execption
'''if __name__=='__main__':
	o=B(5)
	for i in o:
		print i'''
	
