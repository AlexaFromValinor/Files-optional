
f_int = input('File to read:')
print(f_int)
print()
print('Your file:')
with open(f_int) as f:
    for line in f:
        print(line, end='')
    print()
not_exit = True
while (not_exit == True):
    TODO = input('What are we doing? \n (exit,append,read) \n ')
    if (TODO == 'exit'):
        print('bye')
        not_exit = False
    elif (TODO == 'append'):
        with open(f_int,"a") as f:
            st = input('your line:')
            f.write('\n'+st)
        with open(f_int) as f:
            for line in f:
                print(line, end='')
        print()
        print('done')
    elif (TODO == 'read'):
        i1 = int(input('Starting with line:'))
        i2 = int(input('Until line:'))
        with open(f_int) as f:
            i = 0
            for line in f.readlines():
                if i in range(i1-1, i2):
                    print(line, end='')
                i += 1
        print()
