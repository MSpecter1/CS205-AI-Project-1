from queue import PriorityQueue
import NineMenTrench
import time

class Node:
    depth = 0
    state = None
    queue_function = None

    def __init__(self):
        self.solution = []
        return

    def incrementDepth(self):
        self.depth+=1

    def initialize(self, state, q_function):
        # set init state
        self.state = state
        # set function to be used for queue (uniform, misplaced tiles, manhattan)
        self.queue_function = q_function
        return 

    def __lt__(self, other):
        # use queue function to compare   
        return self.queue_function(self) < self.queue_function(other)
    
    def __eq__(self, other):
        # check if state is the same and update depth accordingly  
        if(self.state == other.state):
            self.depth = min(self.depth, other.depth)
            other.depth = min(self.depth, other.depth)
            return True
        return False
    
    def printSolution(self):
        print('\nSolution Path:')
        for i in self.solution:
            print(i)

def UniformCost(node):
    return node.depth

def AStar_MisplacedTiles(node):
    return node.depth + node.state.MisplacedTileHeuristic()

def AStar_ManhattanDistanceAll(node):
    return node.depth + node.state.ManhattanDistanceHeuristicAll()

def AStar_ManhattanOneMisplacedRest(node):
    return node.depth + node.state.ManhattanOneHeuristicMisplacedTilesRest()

def AStar_CostOneMTMD(node):
    return node.depth + node.state.CostOneMTMDHeuristic()
def AStar_CostOneMT(node):
    return node.depth + node.state.CostOneMTHeuristic()

class GeneralSearch:
    # AStar Search to find steps to balance ship
    def search(self, problem, queue_function):
        start = time.time()
        nodes_expanded = 0
        max_queue_size = 0

        expanded = False

        # Create frontier priority queue and a set for all explored nodes
        frontier_nodes = PriorityQueue()
        frontier_list = []
        explored = []

        #  Initialize starting problem state
        InitNode = Node()
        InitNode.initialize(problem.InitialState(), queue_function)
        print("Initial Problem State:")
        InitNode.state.printState()
        frontier_nodes.put(InitNode)
        frontier_list.append(InitNode)

        cnt = 0

        #  Main loop
        while not frontier_nodes.empty():
            # if cnt>10: break
            # cnt+=1
            # for row in explored:
            #     row.state.printState()
            
            # if current queue size is larger, update max_queue_size
            max_queue_size = max(max_queue_size,frontier_nodes.qsize())

            #  Get top node and add to explored set
            node = frontier_nodes.get()
            frontier_list.remove(node)
            explored.append(node)

            # DEBUG print state
            print("Current Node:")
            node.state.printState()
            print("G(N)+H(N) = ", node.queue_function(node), ", Depth:",node.depth, "Time: ", time.time()-start)
            print("\n")

            # Check for solution
            if problem.GoalTest(node.state):
                # found solution
                print("SOLUTION FOUND")
                print("Depth:", node.depth)

                print("---------")
                node.state.printState()
                print("G(N)+H(N) = ", node.queue_function(node), ", Depth:",node.depth, "Time: ", time.time()-start)
                node.printSolution()
                print("---------")

                print("Overall Execution Time: ", time.time()-start)
                print("Nodes Expanded: ", nodes_expanded)
                print("Max Queue Size: ", max_queue_size)
                return 1
            
            # Expand Node with operators
            newNodes = problem.Operate(node)
            expanded = False

            # check if nodes in newNodes are in explored or in frontier
            for n in newNodes:
                n.incrementDepth()
                if not(any(element==n for element in explored) or any(element==n for element in frontier_list)):
                    # put in frontier_nodes if completely new
                    frontier_nodes.put(n)
                    frontier_list.append(n)
                    expanded = True
            
            if expanded: nodes_expanded+=1


        print("No SOLUTION")
        print("Overall Execution Time: ", time.time()-start)
        print("Nodes Expanded: ", nodes_expanded)
        print("Max Queue Size: ", max_queue_size)
        return 0
    

# Interface Code
print("Nine Men in a Trench:\n-------------------------")
print("Heuristics:")
print("0. Uniform Cost")
print("1. AStar Misplaced Tiles")
print("2. AStar Manhattan Distance of All")
print("3. AStar Manhattan of One, Misplaced Tiles for rest")
print("4. AStar CostOneMT with Manhattan Distance")
print("5. AStar CostOneMT")
h = int(input("Please choose a heuristic: "))

print("Problem States:")
print("0. Initial State")
print("1. 12 depth state")

p = input("Please choose a problem: ")

match h:
    case 0: 
        queue_function = UniformCost
    case 1: 
        queue_function = AStar_MisplacedTiles
    case 2: 
        queue_function = AStar_ManhattanDistanceAll
    case 3: 
        queue_function = AStar_ManhattanOneMisplacedRest
    case 4: 
        queue_function = AStar_CostOneMTMD
    case 5: 
        queue_function = AStar_CostOneMT

test = GeneralSearch()
problem = NineMenTrench.NineMenTrench(p)
test.search(problem, queue_function)