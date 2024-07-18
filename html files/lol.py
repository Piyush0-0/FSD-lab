p=int(input("enetr a number:"))
for x in range(0,p):
    for y in range(0,p-x):
        print('*',end='')
    for y in range(0,0+x):
        print(' ',end='')
    for y in range(0,0+x):
        print(' ',end='')
    for y in range(0,p-x):
        print('*',end='')
    print()
for x in range(0,p):
    for y in range(0,1+x):
        print('*',end='')
    for y in range(0,p-x-1):
        print(' ',end='')
    for y in range(0,p-x-1):
        print(' ',end='')
    for y in range(0,1+x):
        print('*',end='')
    print()
    