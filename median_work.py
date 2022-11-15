import math
import numpy as np
class Strategy(object) :
    '''class docstring'''
    def Median(self,itr) :
        '''function docstring'''
        if any(itr) is True :
            if len(itr)>1 :
                for i in itr :
                    if type(i) is int or type(i) is float :
                        continue
                    else :
                        return 'invalid member'
                itr = sorted(itr)
                if len(itr)%2==0 :
                    if len(itr) == 2 :
                        return np.mean(itr)
                    else :
                        idx1 = (len(itr)/2) - 1
                        idx2 = len(itr)/2
                        med = (itr[int(idx1)]+itr[int(idx2)])/2
                        return med
                else :
                    idx = math.ceil((len(itr)/2))-1
                    return itr[idx]
            else :
                return 'low number of members'
        else :
            return 'empty input'

sample = Strategy()
print(sample.Median([1,2,3,4,5,6]))

exit = input('to exit please enter any key :')
