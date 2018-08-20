for rows in range(6):
    for col in range(5):
        if ((col == 0) or (rows == 0 and col < 4) or (rows == 5 and col < 4)):
            print('* ', end='')
        else:
            print(end='')
    print()
