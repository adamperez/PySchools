# Write a function that does a decimal to hexadecimal conversion.
# Hint: Make use of "%x" for hexadecimal format.
def dec2hex(num): 
	gap = "0x0" + "%x" % num
	if len(gap) > 4:
	  sol = "0x" + "%x" % num
	  return sol
	else:
	  return gap