class N(object):
    '''calcultaing 1+2+3+....+n , 1-2+3-.....+-n , -1+2-3+.....-+n'''
    def __init__(self,number) -> None:
        self.n = number
    def claculate(self)->int:
        '''function docstring'''
        c1 = 0
        for i in range(1,self.n+1):
            c1+=i
        c2 = '1-'
        for i in range(2,self.n+1):
            if i == self.n  :
                c2+=str(i)
            elif i%2==0 :
                c2+=f'{str(i)}+'
            else :
                c2+=f'{str(i)}-'
        c3 = '-1+'
        for i in range(2,self.n+1):
            if i == self.n  :
                c3+=str(i)
            elif i%2==0 :
                c3+=f'{str(i)}-'
            else :
                c3+=f'{str(i)}+'
        return f'{c1}\n{eval(c2)}\n{eval(c3)}'

sample = N(int(input('enter a integer number here :')))
print(sample.__doc__)
print(sample.claculate())
exit = input('please enter any key to exit :')
