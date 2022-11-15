# #for hhheeeelllllo or heeeeeeeeelllllooooooooooooo or hheeeeeeeeeeelloo and words like that
# class Hello(object) :
#     '''class docstring'''
#     def __init__(self,text) -> None:
#         self.t = text
#     def Edit(self)->None :
#         '''function docstring'''
#         text_list = self.t.split()
#         new_text_list = list()
#         temp = ''
#         for i in text_list :
#             for j in i :
#                 if j == 'h' :
#                     temp += 'h'
#                     idx1 = i.index(j)+1
#                     for e in i[idx1:] :
#                         if e == 'e' :
#                             temp += 'e'
#                             idx2 = i.index(e)+1
#                             for l in i[idx2:]:
#                                 if l == 'l' :
#                                     temp += 'l'
#                                     idx3 = i.index(l)+1
#                                     for ll in i[idx3:]:
#                                         if ll == 'l' :
#                                             temp += 'l'
#                                             idx4 = i.index(ll)+1
#                                             for o in i[idx4:]:
#                                                 if o == 'o' :
#                                                     temp += 'o'
#                                                     idx5 = i.index(o)+1
#                                                     for o2 in i[idx5:]:
#                                                         if o2 == 'o' :
#                                                             continue
#                                                         else :
#                                                             temp = ''
#                                                             break
#                                                 else : 
#                                                     if o == 'l':
#                                                         continue
#                                                     else :
#                                                         temp = ''
#                                                         break
#                                         else :
#                                             if ll == 'l':
#                                                 continue
#                                             else :
#                                                 break
#                                 else :
#                                     if l == 'e':
#                                         continue
#                                     else :
#                                         break
#                         else :
#                             if e == 'h' :
#                                 continue
#                             else :
#                                 break
#                 else :
#                     break
#             if 'hello' in temp :
#                     new_text_list.append('hello')
#                     temp = ''
#                     continue
#             new_text_list.append(i)
#             temp = ''
#         new_text = ' '.join(new_text_list)
#         return new_text

# while ask :=input('enter a text here :'):
#     sample = Hello(ask)
#     print(sample.Edit())

'''______________________________________________________________________________________________________'''

##for hello in any word like hello in 12545hgfgddfeeeeeeellllll4sf4a5efao
# def analyze(word)->None:
#     '''function docstring'''
#     idx = 0
#     lst = list()
#     temp = ''
#     for i in word :
#         lst.append((i,idx))
#         idx+=1
#     for i in lst :
#         if i[0] == 'h' :
#             if temp != 'h' :
#                 temp += 'h'
#                 c = i[1]+1
#                 new_bug = lst[c:]
#                 break
#     if len(temp) == 1 :
#         for i in new_bug :
#             if i[0] == 'e' :
#                 temp += 'e'
#                 c = i[1]+1
#                 new_bug = lst[c:]
#                 break
#     if len(temp) == 2 :
#         for i in new_bug :
#             if i[0] == 'l' :
#                 temp += 'l'
#                 c = i[1]+1
#                 new_bug = lst[c:]
#                 break
#     if len(temp) == 3 :
#         for i in new_bug :
#             if i[0] == 'l' :
#                 temp += 'l'
#                 c = i[1]+1
#                 new_bug = lst[c:]
#                 break
#     if len(temp) == 4 :
#         for i in new_bug :
#             if i[0] == 'o' :
#                 temp += 'o'
#                 c = i[1]+1
#                 new_bug = lst[c:]
#                 break
#     return temp

# Bug = '1 ahhheeeellllloooou 2 hlelo 3 lahello 4 ohellao 5 hello 6 hwweeeel25loop 7 thello 8 halo 9 heeelo 10 lahlaello 11 helolo 12 hhhhheeeeellllooooo'
# def check(text)->None:
#     '''function doxstring'''
#     bug = text.split()
#     finall = ''
#     for i in bug :
#         if analyze(i) == 'hello' :
#             finall += 'hello '
#         else :
#             finall += i+' '
#     return finall
# print(check(Bug))