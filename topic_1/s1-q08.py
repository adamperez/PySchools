# Write a function, given a string of characters, return the string together with '_'s of the same length.
def underline(title): 

	lineCount = len(title)
	lines = '_' * lineCount
	
	return title + '\n' + lines