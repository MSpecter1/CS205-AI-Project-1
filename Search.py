from queue import PriorityQueue
import NineMenTrench
import time

class UniformCostSearch:

    NMT = NineMenTrench

    # AStar Search to find steps to balance ship
    def search(self, ship_state, manifest_link):
        start = time.time()

        print("No SOLUTION")
        print("Overall Execution Time: ", time.time()-start)
        return 0