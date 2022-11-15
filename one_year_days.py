class Year(object):
    '''class docstring'''
    def __init__(self,day) -> None:
        self.d = day
    def calculate(self)->None:
        '''function docstring'''
        if 1<=self.d<=366:
            one_year_days = [i for i in range(1,367,1)]
            spring = one_year_days[0:93]
            far = spring[0:31]
            ordi = spring[31:62]
            khor = spring[62:]
            summer = one_year_days[93:186]
            tir = summer[0:31]
            mor = summer[31:62]
            shahr = summer[62:]
            fall = one_year_days[186:277]
            mehr = fall[0:30]
            aban = fall[30:60]
            azar = fall[60:]
            winter = one_year_days[277:]
            day = winter[0:30]
            bah = winter[30:60]
            esf = winter[60:]
            if self.d in spring :
                if self.d in far :
                    print(f'bahar - farvardin - {far.index(self.d)+1}')
                elif self.d in ordi :
                    print(f'bahar - ordibehesht - {ordi.index(self.d)+1}')
                else :
                    print(f'bahar - khordad - {khor.index(self.d)+1}')
            elif self.d in summer :
                if self.d in tir :
                    print(f'tabestan - tir - {tir.index(self.d)+1}')
                elif self.d in mor :
                    print(f'tabestan - mordad - {mor.index(self.d)+1}')
                else :
                    print(f'tabestan - sharivar - {shahr.index(self.d)+1}')
            elif self.d in fall :
                if self.d in mehr :
                    print(f'payiz - mehr- {mehr.index(self.d)+1}')
                elif self.d in aban :
                    print(f'payiz - aban - {aban.index(self.d)+1}')
                else :
                    print(f'payiz - azar - {azar.index(self.d)+1}')
            else :
                if self.d in day :
                    print(f'zemestan - day - {day.index(self.d)+1}')
                elif self.d in aban :
                    print(f'zemestan - bahman - {bah.index(self.d)+1}')
                else :
                    print(f'zemestan - esfand - {esf.index(self.d)+1}')
        else :
            print(f'{self.d} is out the range')

while d := input('enter a day here :'):
    temp = Year(int(d))
    temp.calculate()