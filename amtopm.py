class AmToPm(object):
    def __init__(self,time) -> None:
        self.time=time
    def Set(self):
        time_list = self.time.split(':')
        t = []
        for time in time_list:
            t.append(int(time))
        for i in t :
            if i<0:
                print('erorr')
                return
        if t[0]>12:
            print('error')
            return
        elif t[1]>60 :
            print('error')
            return
        else :
            r = ''
            r+=str(t[0]+12)
            r+=":"
            r+=str(t[1])
        print(r)
            
Time = AmToPm(input('enter the time EXAMPLE=12:00:'))
Time.Set()    

import time
print(time.process_time())
exit = input('PLEASE ENTER ANY KEY TO EXIT :')
