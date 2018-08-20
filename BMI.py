n = input('enter the no. of occurrences ')
result = []
for i in range(0,n):
    weight = int(input('enter the weight '))
    height = float(input('enter the height '))
    bmi    = weight/ (height)**2
    result.append(bmi)
    i = i+1

for items in result:
    if result[i] < 18.5:
        print('UnderWeight')
    elif result[i] => 18.5 and result[i] < 25:
        print('NormalWeight')
    elif result[i] => 18.5 and result[i] < 30:
        print('OverWeight')
    else:
        print('Obesity')