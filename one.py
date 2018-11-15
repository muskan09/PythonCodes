def activity01(num1):
	'''Determine if an input number is Even or Odd'''
	if (num1 % 2 == 0):
		return 'Even'
	else:
		return 'Odd'
	
		
def activity02(iv_one, iv_two):
	'''Return the sum of two input values'''
	one_plus_two = iv_one + iv_two
	return one_plus_two

def activity03(num_list):
	'''Given a list of integers, count how many are even'''
	even_count = 0
	odd_count = 0
	for number in num_list:
		if (number % 2 == 0):
			#count = count + 1
			even_count += 1
		else:
			odd_count += 1
	return even_count
	
def activity04(input_string):
	'''Return the input string, backward'''
	return input_string[::-1]
	
