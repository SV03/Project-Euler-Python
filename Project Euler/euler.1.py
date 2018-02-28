def sum_of_div_35(to=10):

	result = 0
	for i in xrange(1,to):
		 if i  % 3 == 0 or i % 5 == 0:
		 	result += i


	return result

print sum_of_div_35()