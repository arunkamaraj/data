def spliting(f):
	words=f.split(' ')
	print words
	return words
def first_word(f):
	print "with out sorting"
	print f.pop(0)
def last_word(f):
	print "with out sorting"
	print f.pop(-1)
def first_word_s(f):
        print "with  sorting"
        print f.pop(0)
def last_word_s(f):
        print "with  sorting"
        print f.pop(-1)
def sorting(w):#
	print sorted(w)
	return sorted(w)
f="i m a good boy"
w=spliting(f)
s=sorting(w)
first_word(w)
last_word(w)
first_word_s(s)
last_word_s(s)



