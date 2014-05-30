import re
def plural(noun):
	if re.search('[sxz]$', noun):
		p=re.sub('$', 'es', noun)
		print p
	elif re.search('[^aeioudgkprt]h$', noun):
		p=re.sub('$', 'es', noun)
		print p
	elif re.search('[^aeiou]y$', noun):
		p= re.sub('y$', 'ies', noun)
		print p
	else:
		p= noun + 's'
		print p

