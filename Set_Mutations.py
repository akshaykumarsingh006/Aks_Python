a = int(input('enter the no. of elements in the Set: '))
A = set(map(int, input('enter the elements: ').strip('').split()))
n = int(input('enter the no. of other Sets: '))
for i in range(n):
    x = (input().split())
    y = set(map(int, input('enter the elements: ').strip('').split()))
    cmd = x[0]
    l = x[1]
    if len(y) > l:
        print('please input the values as per the lenth specified')
    if cmd == 'intersection_update':
        A.intersection_update(y)
    elif cmd == 'update':
        A.update(y)
    elif cmd == 'symmetric_difference_update':
        A.symmetric_difference_update(y)
    elif cmd == 'difference_update':
        A.difference_update(y)
    else:
        print('Please enter the appropriate input: ')

print(sum(A))
