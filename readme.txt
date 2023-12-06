The program is coded in Python
Version Python 3.10.8

The Code Structure:
First there are import statements
Then the command line arguments are accessed.
There are several functions such as 
- gamePlay: to start the game, it checks the moves of computer and the human
- getComputerMove: calls another function to check what should be the optimal move for the computer
- alphaBetaMinMax: to generate the minmax for optimal solution
- finalDecision: to return the final score.


Example to run the code:
python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>

python red_blue_nim.py 3 3 standard human 5

alternatively!! (python red_blue_nim.py 3 2   )

make sure the number of red and blue marbles are integers 
make sure that depth is an integer



**Eval Function**
The alphaBetaMinMax function implements the minimax algorithm with alpha beta pruning.
It uses the depth parameter to control how many levels deep it should search. 
It decrements the depth at each recursive call.

Pruning of branches:
If the depth is larger, then it allows the algorithm to find the optimal solution, 
However,if depth is small it also increases the chances of alpha-beta pruning effectively 
eliminating branches of the search tree that are not relevant to the final decision.
A smaller depth will make the algorithm computate faster but thye result wont be optimal.

So basically, if the depth is limited then the min max tree wont be generated completely 
and the best score will be returned accordingly for the generated branches
