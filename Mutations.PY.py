s = input('enter the string: ')
indpos = int(input('enter the index position '))
letter = input('enter the letter to be entered ')
mystring = s[:(indpos)]+letter+s[(indpos+1):]
print(mystring)