# Soduko_Solver: Python 3.8.8
This program using a backtracking algorithm to solve 3 difficulties of sudoku puzzles.
You can choose to have the algo print so you can visually see it in action.
It times and keeps tracks of the number of back tracks.
The medium and hard difficulties require too many iterations for my computer to crunch.
This highlights the issues with this type of algorithm. Each blank spot in the board could potentially require a backtrack which could bring the iterations to ~75 * 9 = 675.
However each backtrack could have been filled with 75 - 1 * 9 backtracks roughly. This can quickly get into the hundreds of thousands of backtracks to solve the most difficult puzzles.


Cool things I learned:
1.) How to iterate through a section of a 2D array by generating a range of indexs.
  Those indexes could be descrete chunks by using the // operator
  
2.) To keep track of the backtracking path I used a stack, much like how you might keep track of the path
  in a tree traversal search algorithm.
 
