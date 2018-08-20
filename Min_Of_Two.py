l = []
n = int(input('enter the no of occurrences '))
for i in range(0, n):
    nums = list(map(int, input('enter the  nos :').split()))
    l.append(min(nums))
    i = i+1
print('would you like us to show the result :')
a = input().lower
if a == 'yes':
    print(l)
else:
    print('As you wish')






