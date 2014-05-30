import re
def build_match_and_apply_functions(pattern, search, rep):
	def matches_rule(word):
		return re.search(pattern, word)
	def apply_rule(word):
		return re.sub(search, rep, word)
	return (matches_rule, apply_rule)
rules = []
with open('plural4-rules.txt') as pattern_file:
	for line in pattern_file:
		print str(line)
		pattern, search, rep = line.split('|', 2) 
		'''		z= line.split('|',3)
#		print z
		pattern=z[0]
#		print pattern
		search=z[1]
		print search
		rep=z[2]
#		print rep'''
		rules.append(build_match_and_apply_functions(pattern, search, rep))

