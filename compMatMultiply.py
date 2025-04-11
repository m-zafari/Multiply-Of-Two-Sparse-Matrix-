# Mohammad Zafari
# mhdzafari80@gmail.com

def sparse_matrix(compact_arr):

    n_of_compact_column = len(compact_arr[0])
    max_sparse_row = 0
    max_sparse_column = 0

    for i in range(n_of_compact_column): 
        if compact_arr[1][i] > max_sparse_column: 
            max_sparse_column = compact_arr[1][i]
        if compact_arr[0][i] > max_sparse_row:
            max_sparse_row = compact_arr[0][i]    

    sparseMatrix = [[0 for i in range(max_sparse_column+1)] for j in range(max_sparse_row+1)] 

    for k in range(n_of_compact_column):
        sparseMatrix[(compact_arr[0][k])][(compact_arr[1][k])] = compact_arr[2][k] 

    return sparseMatrix

def Multiplication_Matrix(first,second):
    #first   n*k
    #second  k*m
    #result  n*m
    result = [[0 for i in range(len(second[0]))] for j in range(len(first))] 
    for i in range(len(first)):
        for j in range(len(second[0])):
            for k in range(len(second)):
                result[i][j] += first[i][k] * second[k][j]
    return result

def compact_Mat(matrix1):
    size = 0
    for i in range(len(matrix1)): 
	    for j in range(len(matrix1[0])): 
		    if (matrix1[i][j] != 0): 
			    size += 1
    compactMatrix = [[0 for i in range(size)] for j in range(3)]
    
    k = 0
    for i in range(len(matrix1)): 
        for j in range(len(matrix1[0])): 
            if (matrix1[i][j] != 0):
                compactMatrix[0][k] = i
                compactMatrix[1][k] = j
                compactMatrix[2][k] = matrix1[i][j]
                k += 1
    return compactMatrix


compact_1 = [[0, 0, 1, 1, 3, 3],  #row
             [2, 4, 2, 3, 1, 2],  #col
             [3, 4, 5, 7, 2, 6]] #val


compact_2 = [[0, 0, 1, 1, 2, 3, 3],  #row
             [0, 4, 0, 3, 2, 1, 4],  #col
             [2, 4, 8, 3, 6, 2, 8]] #val

sparse1 = sparse_matrix(compact_1)
sparse2 = sparse_matrix(compact_2)
sparse_Multip_result = Multiplication_Matrix(sparse1,sparse2)
final_result=compact_Mat(sparse_Multip_result)


#print
print("\n")
print("the ( first ) arry:(compact sparse)\n")
print(compact_1)
print("\n")
print("the ( second ) arry:(compact sparse)\n")
print(compact_2)
print("\n")
print("the ( first * second ) arry:(compact sparse)\n")
print(final_result)
print("\n")