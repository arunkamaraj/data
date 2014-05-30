class a(object):
    def __init__(self,x):
        self.x = x
    def __iter__(self):
        return self
    def next(self):
        if self.x > 0:
            self.x-=1
            return self.x
        else:
            raise StopIteration
'''if __name__=="__main__": 
	obj = a()
 	for item in obj:
     		print item'''
