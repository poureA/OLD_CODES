import numpy as np  
class matrix_work :
    def check_it(self)->None:
        '''_____'''
        m1_row = int(input('enter number of rows for matrix one :'))
        m1_column = int(input('enter number of  columns for matrix one :'))
        m2_row = int(input('enter number of rows for matrix two :'))
        m2_column = int(input('enter number of  columns for matrix two :'))
        if m1_column == m2_row :
            global matrix_one;global matrix_two
            matrix_one=[]
            matrix_two = []
            child_one = []
            child_two = []
            for i in range(m1_row):
                for j in range(m1_column):
                    child_one.append(int(input('enter a number for matrix one :')))
                matrix_one.append(child_one)
                child_one = []
            for i in range(m2_row):
                for j in range(m2_column):
                    child_two.append(int(input('enter a number for matrix two :')))
                matrix_two.append(child_two)
                child_two = []
        else :
            print('erorr!\nmatrix one columns are not equal with matrix two rows\nplease enter the valid values')
        return matrix_one , matrix_two
    def make_new_matrix(self,matrix_two):
        child = []
        global new_matrix
        new_matrix = []
        index = 0
        for i in range(len(matrix_two[0])):
            for j in matrix_two:
                child.append(j[index])
            new_matrix.append(child)
            child = []
            index += 1
        return new_matrix
    def mul_tiply(self,M1):
        finall_matrix = []
        sum = 0
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                sum += M1[j]*new_matrix[i][j]
            finall_matrix.append(sum)
            sum = 0
        return finall_matrix

mw = matrix_work()
mw.check_it()
mw.make_new_matrix(matrix_two)
output = list(map(mw.mul_tiply,[i for i in matrix_one]))
with open('D:\\text\\matrix_work.txt','w+') as output_file :
    output_file.write(f'the resul is :\n\nmatrix one :\n{np.array(matrix_one)}\n\nmatrix two :\n{np.array(matrix_two)}\n\nmatrix one * matrix two =\n{np.array(output)}')
exit = input('please enter any key to exit :')
