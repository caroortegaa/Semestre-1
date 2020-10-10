año = int(input())
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('True')
        else:
            print('False')
    else:
        print('False')
else:
    print('False')
