import numpy as np
vals = 8,1,6,3,5,7,4,9,1,2,3,4,5,6,7,10
def make_matrix(*args)->None:
    '''function docstring'''
    arr = np.array([*args],dtype='float64')
    sh = input(f'numbers of members = {len(arr[0])} please enter the shape of the matrix example(2,5):')
    newarr = arr.reshape(eval(sh))
    return newarr
    
def ismagic(matrix)->None:
    '''function docstring'''
    Sum = sum(matrix[0])
    rows_sums = list()
    for row in matrix :
        rows_sums.append(sum(row))
    tmatrix = np.transpose(matrix)
    cols_sums =list()
    for col in tmatrix :
        cols_sums.append(sum(col))
    gh_list = list()
    idx = 0
    for i in range(len(matrix)):
        gh_list.append(matrix[idx][idx])
        idx+=1
    gh_sum = [sum(gh_list)]
    finall_list = [rows_sums,cols_sums,gh_sum]
    for i in finall_list :
        for j in i :
            if j != Sum :
                return f'False :( {finall_list}'
    return f'True :)  {finall_list}'

print(ismagic(make_matrix(vals)))
exit = input('please enter any key to exit :')
