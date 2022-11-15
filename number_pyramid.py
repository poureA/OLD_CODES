n = int(input('enter a number here :'))
print(1)
if n!=0 :
    if n>0 :
        c = 0
        for i in range(2,n+1):
            for j in range(i):
                c+=i
                print(c,end=' ')
            print('\n')
            c = 0
    else :
        print('negative')
else :
    print('zero')
exit = input('please enter to exit :')
