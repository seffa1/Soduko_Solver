# Soduko_Solver: Python 3.8.8
This program using an iterative backtracking algorithm to solve 3 difficulties of sudoku puzzles.
You can choose to have the algo print so you can visually see it in action.
It times and keeps tracks of the number of back tracks and total iterations.

Cool things I learned:
1.) How to iterate through a section of a 2D array by generating a range of indexs.
  Those indexes could be descrete chunks by using the // operator
  
2.) To keep track of the backtracking path I used a stack, much like how you might keep track of the path
  in a tree traversal search algorithm.
  
3.) Using a recursive appoach worked on the easy board, but a stack overflow was hit on the medium/hard boards
 
