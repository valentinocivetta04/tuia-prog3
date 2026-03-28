from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        frontera = QueueFrontier()
        frontera.add(root)
        # Si el estado inicial es el objetivo
        if grid.objective_test(root.state):
            return Solution(root, reached)
        
        node = root
        
        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            
            n = frontera.remove()

            for a in grid.actions(n.state):
                s1 = grid.result(n.state, a)
                if s1 not in reached:
                    n1= Node(s1,n,a,n.cost + grid.individual_cost(n.state,a))
                    if grid.objective_test(s1):
                        return Solution(n1)
                    reached[s1] = True
                    frontera.add(n1)
        
        
        return NoSolution(reached)
