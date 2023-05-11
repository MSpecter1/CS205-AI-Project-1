from queue import PriorityQueue
import NineMenTrench
import time
import copy

class Node:
    depth = 0
    state = None
    queue_function = None

    def __init__(self, state, q_function):
        # set init state
        self.state = state
        # set function to be used for queue (uniform, misplaced tiles, manhattan)
        self.queue_function = q_function
        return 0

    def __lt__(self, other):
        # use queue function to compare   
        return self.queue_function(self) < self.queue_function(other)

def UniformCost(node):
    return node.depth

def AStar_MisplacedTiles(node):
    return node.depth + node.state.MisplacedTileHeuristic()

def AStar_ManhattanDistance(node):
    return node.depth + node.state.ManhattanDistanceHeuristic()

class GeneralSearch:
    # Create frontier priority queue and a set for all explored nodes
    frontier_nodes = PriorityQueue()
    explored = {} 

    # AStar Search to find steps to balance ship
    def search(self, problem, queue_function):
        start = time.time()

        #  Initialize starting problem state
        InitNode = Node(problem.InitialState(), queue_function)
        self.frontier_nodes.put(InitNode)

        #  Main loop
        while not self.frontier_nodes.empty():
            
            #  Get top node
            node = self.frontier_nodes.get()

            # Check for solution
            if problem.GoalTest(node.state):
                # found solution
                return 1
            
            # Expand Node with operators, 3*distance (1 per direction) in total for NMT
            for i in range(0, problem.operators): 
                #  deep copy node so that new state is created/copied
                NewNode = copy.deepcopy(node)

                # check if explored
                # check if in frontier_nodes

                # put in frontier_nodes if completely new
                self.frontier_nodes.put(NewNode)

        print("No SOLUTION")
        print("Overall Execution Time: ", time.time()-start)
        return 0
    
test = GeneralSearch()
problem = NineMenTrench()
queue_function = UniformCost()
GeneralSearch.search(problem, queue_function)