def my_leet(my_text):
    my_list=['a','4','b','8','c','<','d','|)','e','3','f','7','g','9','h','#','i','1','j','_/','k','|','l','|_','m','&','n','!','o','0','p','|0','q','(,)','r','|2','s','$','t','-|-','u','|_|','v','\/','w','\/\/','x','*','y','?','z','_/_']
    r = ''
    for i in my_text:
        if i in my_list:
            r+=my_list[(my_list.index(i)+1)]
        else :
            r += i
    return r

while text:=input('enter your note here :') :
    print(my_leet(text))
