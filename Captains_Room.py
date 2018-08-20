k = int(input('enter the value of k: '))
rooms = list(map(int, input('enter the room no.: ').strip('').split()))
q = set(rooms)
for items in q:
    cnt = rooms.count(items)
    if cnt == 1:
        print(items)