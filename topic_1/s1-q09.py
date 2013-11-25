# Use one or more string methods in above examples, extract the substring
# surrounded by 'xyz' at the beginning and end. Replace the ',' in the substring with '|'.
# and remove all trailing space.

str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
idx1 = str1.find('xyz')                    # get the position of 'xyz'
idx2 = str1.find('xyz', idx1+1)            # get the next 'xyz'
str1 = str1[idx1+3:idx2].replace(',','|')    # replace ',' with '|'
str1 = str1.strip()                             # strip trailing spaces. 
