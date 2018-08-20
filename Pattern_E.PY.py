for row in range(7):
    for col in range(4):
        if((col==0) or (row==0 and col<3) or (row==3 and col<2) or (row==6 and col<3)):
            print('* ', end='')
        else:
            print(end=' ')
    print()