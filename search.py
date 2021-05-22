import util

class SearchProblem:

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #util.raiseNotDefined()
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    fringe = util.Stack()
    start = problem.getStartState()
    visited = [start]

    for pos, direction, c in problem.getSuccessors(start):
    	fringe.push((pos, [direction]))

    while not fringe.isEmpty():
    	currPos, currDir = fringe.pop()
  
    	if not (currPos in visited):
    		if problem.isGoalState(currPos):
    			return currDir
    		visited += [currPos]
    		for pos, direction, c in problem.getSuccessors(currPos):
    			if not (pos in visited):
    				temp = currDir + [direction]
    				fringe.push((pos, temp))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    start = problem.getStartState()
    visited = [start]

    for pos, direction, c in problem.getSuccessors(start):
    	fringe.push((pos, [direction]))

    while not fringe.isEmpty():
    	currPos, currDir = fringe.pop()
  
    	if not (currPos in visited):
    		if problem.isGoalState(currPos):
    			return currDir
    		visited += [currPos]
    		for pos, direction, c in problem.getSuccessors(currPos):
    			if not (pos in visited):
    				temp = currDir + [direction]
    				fringe.push((pos, temp))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    visited = [start]

    for pos, direction, c in problem.getSuccessors(start):
    	fringe.push((pos, [direction]), c)

    while not fringe.isEmpty():
    	currPos, currDir = fringe.pop()
  
    	if not (currPos in visited):
    		if problem.isGoalState(currPos):
    			return currDir
    		visited += [currPos]
    		for pos, direction, c in problem.getSuccessors(currPos):
    			if not (pos in visited):
    				temp = currDir + [direction]
    				newCost = problem.getCostOfActions(currDir) + c
    				fringe.push((pos, temp), newCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    start = problem.getStartState()
    visited = [start]

    for pos, direction, c in problem.getSuccessors(start):
    	fringe.push((pos, [direction]), c + heuristic(pos, problem))

    while not fringe.isEmpty():
    	currPos, currDir = fringe.pop()
  
    	if not (currPos in visited):
    		if problem.isGoalState(currPos):
    			return currDir
    		visited += [currPos]
    		for pos, direction, c in problem.getSuccessors(currPos):
    			if not (pos in visited):
    				temp = currDir + [direction]
    				newCost = problem.getCostOfActions(currDir) + c + heuristic(pos,problem)
    				fringe.push((pos, temp), newCost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
