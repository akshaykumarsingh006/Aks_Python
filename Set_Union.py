n = int(input('no.of student for english: '))
N = set(map(int, input().strip('').split()))
m = int(input('no.of student for french: '))
M = set(map(int, input().strip('').split()))
q = len(N)+len(M) - len(N.intersection(M))
print(q)