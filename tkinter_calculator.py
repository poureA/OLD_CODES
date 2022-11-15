import tkinter as tk 
root = tk.Tk()
root.title('calculator')
op = ''
inp = tk.StringVar()
board = tk.Entry(font=('arial','20',),bg='gray',bd='15',justify='right',insertborderwidth=4,textvariable=inp).grid(columnspan=4)
def buttons(numbers)->None:
    global op
    op+=str(numbers)
    inp.set(op)
def result()->None:
    global op
    finall = str(eval(op))
    inp.set(finall)
    op = ''
def clean_it()->None:
    global op
    op = ''
    inp.set(op)
bt0 = tk.Button(root,text='0',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(0)).grid(row=1,column=0)
bt1 = tk.Button(root,text='1',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(1)).grid(row=1,column=1)
bt2 = tk.Button(root,text='2',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(2)).grid(row=1,column=2)
bt3 = tk.Button(root,text='3',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(3)).grid(row=1,column=3)
bt4 = tk.Button(root,text='4',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(4)).grid(row=2,column=0)
bt5 = tk.Button(root,text='5',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(5)).grid(row=2,column=1)
bt6 = tk.Button(root,text='6',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(6)).grid(row=2,column=2)
bt7 = tk.Button(root,text='7',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(7)).grid(row=2,column=3)
bt8 = tk.Button(root,text='8',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(8)).grid(row=3,column=0)
bt9 = tk.Button(root,text='9',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(9)).grid(row=3,column=1)
plus = tk.Button(root,text='+',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('+')).grid(row=3,column=2)
dif= tk.Button(root,text='-',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('-')).grid(row=3,column=3)
div = tk.Button(root,text='/',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('/')).grid(row=4,column=0)
zrb = tk.Button(root,text='*',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('*')).grid(row=4,column=1)
clr = tk.Button(root,text='C',padx='18',pady='18',bg='white',bd='2',fg='red',command=clean_it).grid(row=4,column=2)
res = tk.Button(root,text='=',padx='18',pady='18',bg='white',bd='2',fg='black',command=result).grid(row=4,column=3)
root.mainloop()



'''___________________________________________________________________________________________'''




#import tkinter as tk 
# class cal:
#     def do_it():
#         root = tk.Tk()
#         root.title('calculator')
#         global op
#         op = ''
#         global inp
#         inp = tk.StringVar()
#         board = tk.Entry(font=('arial','20',),bg='gray',bd='15',justify='right',insertborderwidth=4,textvariable=inp).grid(columnspan=4)
#         def buttons(numbers)->None:
#             global op
#             op+=str(numbers)
#             inp.set(op)
#         def result()->None:
#             global op
#             finall = str(eval(op))
#             inp.set(finall)
#             op = ''
#         def clean_it()->None:
#             global op
#             op = ''
#             inp.set(op)
#         bt0 = tk.Button(root,text='0',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(0)).grid(row=1,column=0)
#         bt1 = tk.Button(root,text='1',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(1)).grid(row=1,column=1)
#         bt2 = tk.Button(root,text='2',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(2)).grid(row=1,column=2)
#         bt3 = tk.Button(root,text='3',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(3)).grid(row=1,column=3)
#         bt4 = tk.Button(root,text='4',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(4)).grid(row=2,column=0)
#         bt5 = tk.Button(root,text='5',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(5)).grid(row=2,column=1)
#         bt6 = tk.Button(root,text='6',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(6)).grid(row=2,column=2)
#         bt7 = tk.Button(root,text='7',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(7)).grid(row=2,column=3)
#         bt8 = tk.Button(root,text='8',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(8)).grid(row=3,column=0)
#         bt9 = tk.Button(root,text='9',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons(9)).grid(row=3,column=1)
#         plus = tk.Button(root,text='+',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('+')).grid(row=3,column=2)
#         dif= tk.Button(root,text='-',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('-')).grid(row=3,column=3)
#         div = tk.Button(root,text='/',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('/')).grid(row=4,column=0)
#         zrb = tk.Button(root,text='*',padx='18',pady='18',bg='white',bd='2',fg='blue',command=lambda:buttons('*')).grid(row=4,column=1)
#         clr = tk.Button(root,text='C',padx='18',pady='18',bg='white',bd='2',fg='red',command=clean_it).grid(row=4,column=2)
#         res = tk.Button(root,text='=',padx='18',pady='18',bg='white',bd='2',fg='black',command=result).grid(row=4,column=3)
#         root.mainloop()

# cal.do_it()