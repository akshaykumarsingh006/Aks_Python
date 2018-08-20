mystring = input('enter the string: \n ' '\n')

length = len(mystring)
for rows in range(length):
    for col in range(rows+1):
        print(mystring[col], end= '')
    print()