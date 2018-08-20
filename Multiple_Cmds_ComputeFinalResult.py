n = int(input('enter the no. of elements in the set :'))
s = set(map(int, input('enter the Set elements: ').strip('').split()))
N = int(input('enter the no.of commands: '))
for i in range(N):
    x = input().split()
    cmd = x[0]
    if cmd == 'pop':
        s.pop()
    elif cmd == 'discard':
        s.discard(int(x[1]))
    elif cmd == 'remove':
        s.remove(int(x[1]))
    else:
        print('wrong input')
sum(s)
