# Combine the values of two dictionaries having same key
# Python code to demonstrate combining
# two dictionaries having same key

from collections import Counter

# initialising dictionaries
ini_dictionary1 = Counter({'nikhil': 1, 'akash' : 5,
					'manjeet' : 10, 'akshat' : 15})
ini_dictionary2 = Counter({'akash' : 7, 'akshat' : 5,
										'm' : 15})

# printing initial dictionaries
print ("initial 1st dictionary", str(ini_dictionary1))
print ("initial 2nd dictionary", str(ini_dictionary2))

# combining dictionaries
# using Counter
final_dictionary = ini_dictionary1 + ini_dictionary2

# printing final result
print ("final dictionary", str(final_dictionary))
