mystring = input('Enter the string: ')
result = []
for i in range (len(mystring)):
    if mystring[i].isupper():
        result.append(mystring[i].lower())
    else:
        result.append(mystring[i].upper())

print (''.join(result))