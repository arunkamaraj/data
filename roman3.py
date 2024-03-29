def to_roman(n):
	'''convert integer to Roman numeral'''
	if not (0 < n < 4000):
		raise OutOfRangeError('number out of range (must be 1..3999)')
	result = ''
	for numeral, integer in roman_numeral_map:
		while n >= integer:
			result += numeral
			n -= integer
	return result

class OutOfRangeError(ValueError):
	pass



