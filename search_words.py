class Match(object):
    '''class docstring'''
    class Search :
        '''class docstring'''
        def full_search(self,text1,text2,c=False)->list :
            '''function docstring'''
            text1_list = text1.split()
            text2_list = text2.split()
            r = ''
            lst = []
            for i in text2_list :
                for j in range(len(i)) :
                    for k in i[j:] :
                        r+=k
                        if r in text1_list :
                            lst.append(r)
                    r  = ''
            if c :
                return (lst,len(lst))
            return lst
        def normal_search(self,text1,text2,c=False)->list :
            '''function docstring'''
            text1_list = text1.split()
            text2_list = text2.split()
            lst = []
            for i in text1_list :
                for j in text2_list :
                    if i in j :
                        lst.append(i)
            if c :
                return (lst,len(lst))
            return lst

sample = Match.Search()
t1 = 'tehraniha dar tehran zendegi mikonand'
t2 = '@@@@tehraniha! #zendegi popopopoiii()('
print(sample.full_search(t1,t2,c=True))
exit = input('please enter any key to exit :')
