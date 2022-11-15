import tkinter as tk
base = tk.Tk()
#base.geometry('600x500')
ent = tk.Entry(base,show='*')
ent.grid()
showlbl = tk.Label(base,bg='white')
showlbl.grid()
def convert():
    inpt = ent.get()
    my_list=['a','4','b','8','c','<','d','|)',
    'e','3','f','7','g','9','h','#','i','1','j','_/','k',
    '|','l','|_','m','&','n','!','o','0','p','|0','q','(,)','r','|2','s','$','t','-|-','u','|_|',
    'v','\/','w','\/\/','x','*','y','?','z','_/_']
    r = ''
    for i in inpt:
        if i in my_list:
            r+=my_list[(my_list.index(i)+1)]
        else :
            r += i
    showlbl = tk.Label(base)
    showlbl.destroy()
    showlbl = tk.Label(base,text=r)
    showlbl.grid(row=1)
    ent.delete(0,tk.END)
convertbtn = tk.Button(base,text='convert',command=convert)
convertbtn.grid()
base.title('convertor')
base.mainloop()