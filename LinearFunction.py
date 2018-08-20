a = []
n = int(input('enter the no. of cases: '))
for i in range(0,n):
    var1, var2, var3, var4 = list(map(int,input().split()))
    res1 = round((var3 - var1)/(var4 - var2), 2)
    res2 = round(var2 - (res1*var1),2)
    a.append((res1, res2))
    i = i+1

ask = input('would you like to see the output yes or no :' )
if ask == 'yes':
    print(a)
else:
    print('as you wish...Good Bye.!')
