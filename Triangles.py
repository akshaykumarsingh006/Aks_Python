n = int(input('Enter the no. of triplets'))
for i in range(0, n):
    x, y, z = list(map(int, input('enter the sides of triangle: ').split()))
    i = i + 1

# logic to check if the given sides form triangle
if ((x + y) > z or (y + z) > x or (z + x) > y):
    print('the sides {} form a triangle'.format(x, y, z))
else:
    print('This is not a triangle')