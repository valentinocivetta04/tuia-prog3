from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontera = StackFrontier()
        frontera.add(root)

        # Si el estado inicial es el objetivo
        if grid.objective_test(root.state):
            return Solution(root)
        
        while True:
            if frontera.is_empty():
                return NoSolution(expanded)
            
            n = frontera.remove()

            if n.state in expanded:
                continue

            expanded[n.state] = True

            for a in grid.actions(n.state):
                s = grid.result(n.state, a)
                if s not in expanded:
                    n2 = Node(value="",state=s,parent=n,action=a,
                              cost=n.cost + grid.individual_cost(n.state, a))
                    if grid.objective_test(s):
                        return Solution(n2, expanded)
                    
                    frontera.add(n2)



        
