class NineMenTrench:
    operators = 3

    def InitialState():
        return 0
    
    def GoalTest(state):
        return 0
    
    def MisplacedTileHeuristic():
        return 0

    def ManhattanDistanceHeuristic():
        return 0
    
    def Operate(dir):
        return 0

class TrenchState:

    depth = 0
    state = None
    size = 0
    men = 0

    def InitializeTrench(self, size, men):
        # 0 is an open spot, -1 is invalid, other #s represent people
        self.state = [[None for i in range(size)] for j in range(2)]
        self.size = size
        self.men = men
        other = True # every other spot is a recess in the top row, aside from 3 spaces in the front and 2 spaces in the back
        cnt = 2
        for row in range(0,2):
            for col in range(0,size):
                if row == 0 and col > 2 and col <= size-2 and other:
                    # initialize top row with recesses
                    self.state[row][col] = 0
                    other = False
                elif other==False:
                    other = True

                if row == 1 and col > 0:
                    # initialize trench with men
                    if cnt <= men:
                        self.state[row][col] = cnt
                        cnt+=1
                    else:
                        self.state[row][col] = 1
                        break
                elif row == 1:
                    self.state[row][col] = 0
        return 0
    
    def printState(self):
        for row in self.state:
            print(row)

    def getPosMan(self, man):
        row_num = 0
        for row in self.state:
            # print("TEST",row)
            try:
                col = row.index(man)
            except:
                row_num+=1
                continue
            return (row_num,col)

    def operate(self, man, dir, dist):
        # Move a single man in direction dir, with dist # of spaces
        # dir = 0, move left
        # dir = 1, move up or down
        # dir = 2, move right
        if man>self.men:
            return -1 # error
        
        pos = self.getPosMan(man)
        if dir == 0:
            #  Check if move is possible (no obstacles in left range)
            target = self.state[pos[0]][pos[1]-dist]
            if target == 0 and all(space == 0 for space in self.state[pos[0]][0:pos[1]]):
                self.state[pos[0]][pos[1]-dist] = man
                self.state[pos[0]][pos[1]] = 0
            return 0
        elif dir == 1:
            #  Check if move is possible (no obstacle above/below)
            target_row = 0
            if pos[0] == 0:
                target_row = 1
            elif pos[0] == 1:
                target_row = 0
            target = self.state[target_row][pos[1]]
            if target == 0:
                self.state[target_row][pos[1]] = man
                self.state[pos[0]][pos[1]] = 0
            return 0
        elif dir == 2:
            #  Check if move is possible (no obstacles in right range)
            target = self.state[pos[0]][pos[1]+dist]
            if target == 0 and all(space == 0 for space in self.state[pos[0]][pos[1]+1:pos[1]+dist]):
                self.state[pos[0]][pos[1]+dist] = man
                self.state[pos[0]][pos[1]] = 0
            return 0
        
        return 0

def test():
    test = TrenchState()
    test.InitializeTrench(10, 9)
    print("INITIAL STATE:")
    test.printState()

    print("\n")
    print("TEST: LEFT")
    test.operate(2,0,1)
    test.printState()
    print("\n")
    print("TEST: LEFT INVALID")
    test.operate(3,0,2)
    test.printState()
    print("\n")
    print("TEST: UP")
    test.operate(4,1,1)
    test.printState()
    print("\n")
    print("TEST: DOWN")
    test.operate(4,1,1)
    test.printState()
    print("\n")
    print("TEST: RIGHT")
    test.operate(2,2,1)
    test.printState()

test()