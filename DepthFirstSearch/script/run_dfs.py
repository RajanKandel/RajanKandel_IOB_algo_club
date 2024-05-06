
from DFS_Sudoku import DFS_solve

print ("\n\nTesting on easy 6x6 grid...")
grid = [[6,0,0,0,0,0],
      [0,0,1,3,0,6],
      [0,0,4,0,0,0],
      [1,2,0,0,0,0],
      [0,0,0,0,0,4],
      [3,0,5,0,0,0]]

print ("Problem:")
for row in grid:
      print (row)

DFS_solve(grid)