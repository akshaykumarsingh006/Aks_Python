s = input()
kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in 'aeiou':
        kevsc = kevsc + (len(s)-i)
    else:
        stusc = stusc + (len(s)-i)

if kevsc > stusc:
    print('Kevin', kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")