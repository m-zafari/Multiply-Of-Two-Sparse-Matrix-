due to the fact that most of a sparse matrix is consist of zero(0), so we can just store it by its non zero values with using an array of size (num of values * 3)

compact_1 = [[0, 0, 1, 1, 3, 3], [2, 4, 2, 3, 1, 2], [3, 4, 5, 7, 2, 6]]
For example sparse_matrix[0][2]= [3], sparse_matrix[0][4]= [4] and etc.
in this way we can store a sparse matrix with more compact form.
this code gets two compact format and multiply them and outputs the result compact format.
