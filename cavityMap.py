#Hacker rank challenge (Level: Easy)
#You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
#We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth.
#Two cells are adjacent if they have a common side, or edge.

#Find all the cavities on the map and replace their depths with the uppercase character X.
'''
Example
grid = ['989', 191', '111']
The grid is rearranged for clarity:

989
191
111
Return:

989
1X1
111
'''

def cavityMap(grid):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j - 1] < grid[i][j] and\
               grid[i - 1][j] < grid[i][j] and\
               grid[i + 1][j] < grid[i][j] and\
               grid[i][j + 1] < grid[i][j]:
               
                row_cp = list(grid[i])
                print(row_cp, '!!!', i + 1)
                row_cp[j] = 'X'
                grid[i] = ''.join(row_cp)
                #grid_cp[i][j] = 'X'
    return grid
