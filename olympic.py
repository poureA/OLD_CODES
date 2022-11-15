import random as rn 
import pandas as pd 
temp = []
medals = []
for i in range(6):
    for j in range(3):
        temp.append(rn.randint(0,10))
    medals.append(temp)
    temp = []
years = [i for i in range(1370,1376)]
class Report(object):
    def __init__(self,years,medals) -> None:
        self.y = years
        self.m = medals
    def report(self):
        total_medals = 0
        total_golds = 0
        years_medals = []
        gold_years = []
        point = 0
        point_years = []
        over_10 = 0
        for i in self.m :
            total_golds+=i[0]
            years_medals.append(sum(i))
            gold_years.append(i[0])
            point += ((i[0]*3)+(i[1]*2)+i[2])
            point_years.append(point)
            point = 0
            for j in i :
                total_medals+=j
        for i in point_years :
            if i>10 :
                over_10 += 1
        idx = years_medals.index((max(years_medals)))
        gidx = gold_years.index((max(gold_years)))
        n = 0
        zero_years = []
        for i in self.m :
            if any(i) is False :
                val = self.y[n]
                zero_years.append(val)
                n+=1
                continue
            n+=1
        P = list()
        for i in range(len(point_years)):
            tup = (self.y[i],point_years[i])
            P.append(tup)
        message = f'the resul\nthe performance :\n{pd.DataFrame(self.m,index=self.y,columns=["gold","silver","bronze"])}\ntotal medals : {total_medals}\ntotal gold medals :{total_golds}\nyears with no medals : {zero_years}\nmost succesfull year : {self.y[idx]}\ngolden year : {self.y[gidx]}\neach year point : {P}\nnumber of years with over 10 point : {over_10}'
        path = 'D:\\demo\\olympic.txt'
        with open(path,'w') as file :
            file.write(message)
        print(f'done\nyou can check the result in file : {path}')

country = Report(years,medals)
country.report()
exit = input('please enter any key to exit :')
