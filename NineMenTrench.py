import copy

class TrenchState:
    array_state = None
    size = 0
    men = 0

    def InitializeTrench(self, size, men):
        # 0 is an open spot, NONE is invalid, other #s represent people
        self.array_state = [[None for i in range(size)] for j in range(2)]
        self.size = size
        self.men = men
        other = True # every other spot is a recess in the top row, aside from 3 spaces in the front and 2 spaces in the back
        cnt = 2
        for row in range(0,2):
            for col in range(0,size):
                if row == 0 and col > 2 and col <= size-2 and other:
                    # initialize top row with recesses
                    self.array_state[row][col] = 0
                    other = False
                elif other==False:
                    other = True

                if row == 1 and col > 0:
                    # initialize trench with men
                    if cnt <= men:
                        self.array_state[row][col] = cnt
                        cnt+=1
                    else:
                        self.array_state[row][col] = 1
                        break
                elif row == 1:
                    self.array_state[row][col] = 0

        # self.array_state[1][0] = 2
        # self.array_state[1][1] = 3
        # self.array_state[1][2] = 5
        # self.array_state[1][3] = 6
        # self.array_state[1][4] = 8
        # self.array_state[1][5] = 9
        # self.array_state[1][6] = 0
        # self.array_state[1][7] = 0
        # self.array_state[1][8] = 0
        # self.array_state[1][9] = 1

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 7
        # self.array_state[0][7] = 0

        # /////////////////////

        # self.array_state[1][0] = 2
        # self.array_state[1][1] = 3
        # self.array_state[1][2] = 5
        # self.array_state[1][3] = 6
        # self.array_state[1][4] = 8
        # self.array_state[1][5] = 9
        # self.array_state[1][6] = 0
        # self.array_state[1][7] = 0
        # self.array_state[1][8] = 0
        # self.array_state[1][9] = 0

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 7
        # self.array_state[0][7] = 1

        # /////////////////////

        # self.array_state[1][0] = 2
        # self.array_state[1][1] = 3
        # self.array_state[1][2] = 0
        # self.array_state[1][3] = 0
        # self.array_state[1][4] = 5
        # self.array_state[1][5] = 6
        # self.array_state[1][6] = 7
        # self.array_state[1][7] = 8
        # self.array_state[1][8] = 9
        # self.array_state[1][9] = 1

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 0
        # self.array_state[0][7] = 0

        # 
        
        # self.array_state[1][0] = 2
        # self.array_state[1][1] = 3
        # self.array_state[1][2] = 5
        # self.array_state[1][3] = 6
        # self.array_state[1][4] = 8
        # self.array_state[1][5] = 0
        # self.array_state[1][6] = 0
        # self.array_state[1][7] = 0
        # self.array_state[1][8] = 7
        # self.array_state[1][9] = 9

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 1
        # self.array_state[0][7] = 0

        # 
        # self.array_state[1][0] = 2
        # self.array_state[1][1] = 3
        # self.array_state[1][2] = 5
        # self.array_state[1][3] = 6
        # self.array_state[1][4] = 0
        # self.array_state[1][5] = 0
        # self.array_state[1][6] = 0
        # self.array_state[1][7] = 0
        # self.array_state[1][8] = 7
        # self.array_state[1][9] = 9

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 1
        # self.array_state[0][7] = 8

        # 
        # self.array_state[1][0] = 0
        # self.array_state[1][1] = 2
        # self.array_state[1][2] = 3
        # self.array_state[1][3] = 0
        # self.array_state[1][4] = 5
        # self.array_state[1][5] = 6
        # self.array_state[1][6] = 7
        # self.array_state[1][7] = 8
        # self.array_state[1][8] = 9
        # self.array_state[1][9] = 1

        # self.array_state[0][3] = 4
        # self.array_state[0][5] = 0
        # self.array_state[0][7] = 0
        return 0
    
    def __eq__(self, other):
        # check if state array is the same 
        return self.array_state == other.array_state

    def printState(self):
        for row in self.array_state:
            print(row)

    def getPosMan(self, man):
        row_num = 0
        for row in self.array_state:
            # print("TEST",row)
            try:
                col = row.index(man)
            except:
                row_num+=1
                continue
            return (row_num,col)

    def moveLeft(self, pos, man, dist):
        #  Check if move is possible (no obstacles in left range)
        # target = self.array_state[pos[0]][pos[1]-dist]
        try:
            target = self.array_state[pos[0]][pos[1]-dist]
            if(pos[1]-dist<0): return 0
        except:
            return 0
        # if man==9: print("Target POS:", pos[1]-dist, ", val= ",target)
        if target == 0 and all(space == 0 for space in self.array_state[pos[0]][pos[1]-dist:pos[1]]):
            self.array_state[pos[0]][pos[1]-dist] = man
            self.array_state[pos[0]][pos[1]] = 0
            return 1
        return 0
    
    def moveUpDown(self, pos, man, dist):

        match dist:
            case 0: # move up
                #  Check if move is possible (no obstacle above/below)
                target_row = 0
                target = self.array_state[target_row][pos[1]]
                if target == 0:
                    self.array_state[target_row][pos[1]] = man
                    self.array_state[pos[0]][pos[1]] = 0
                    return 1
                return 0
            case 1: # move down
                #  Check if move is possible (no obstacle above/below)
                target_row = 1
                target = self.array_state[target_row][pos[1]]
                if target == 0:
                    self.array_state[target_row][pos[1]] = man
                    self.array_state[pos[0]][pos[1]] = 0
                    return 1
                return 0

    def moveRight(self, pos, man, dist):
        #  Check if move is possible (no obstacles in right range)
        # target = self.array_state[pos[0]][pos[1]+dist]
        try:
            target = self.array_state[pos[0]][pos[1]+dist]
            if(pos[1]+dist>9): return 0
        except:
            return 0
        if target == 0 and all(space == 0 for space in self.array_state[pos[0]][pos[1]+1:pos[1]+dist]):
            self.array_state[pos[0]][pos[1]+dist] = man
            self.array_state[pos[0]][pos[1]] = 0
            return 1
        return 0

    def operate(self, man, dir, dist):
        # Move a single man in direction dir, with dist # of spaces
        # dir = 0, move left
        # dir = 1, move up or down
        # dir = 2, move right
        if man>self.men:
            return -1 # error
        
        pos = self.getPosMan(man)
        if dir == 0:
            return self.moveLeft(pos,man,dist)
        elif dir == 1:
            return self.moveUpDown(pos,man,dist)
        elif dir == 2:
            return self.moveRight(pos,man,dist)
        return 0

    # def operate(self, man, dir, dist):
    #     # Move a single man in direction dir, with dist # of spaces
    #     # dir = 0, move left
    #     # dir = 1, move up or down
    #     # dir = 2, move right
    #     if man>self.men:
    #         return -1 # error
        
    #     pos = self.getPosMan(man)
    #     # if (pos[1]-dist<0 and dir==0) or (dir==2 and pos[1]+dist>9):
    #     #     # print(man,pos[1], dist)
    #     #     return 0
    #     if dir == 0:
    #         #  Check if move is possible (no obstacles in left range)
    #         # target = self.array_state[pos[0]][pos[1]-dist]
    #         try:
    #             target = self.array_state[pos[0]][pos[1]-dist]
    #             if(pos[1]-dist<0): return 0
    #         except:
    #             return 0
    #         # if man==9: print("Target POS:", pos[1]-dist, ", val= ",target)
    #         if target == 0 and all(space == 0 for space in self.array_state[pos[0]][pos[1]-dist:pos[1]]):
    #             self.array_state[pos[0]][pos[1]-dist] = man
    #             self.array_state[pos[0]][pos[1]] = 0
    #             return 1
    #         return 0
    #     elif dir == 1:
    #         #  Check if move is possible (no obstacle above/below)
    #         target_row = 0
    #         if pos[0] == 0:
    #             target_row = 1
    #         elif pos[0] == 1:
    #             target_row = 0
    #         target = self.array_state[target_row][pos[1]]
    #         if target == 0:
    #             self.array_state[target_row][pos[1]] = man
    #             self.array_state[pos[0]][pos[1]] = 0
    #             return 1
    #         return 0
    #     elif dir == 2:
    #         #  Check if move is possible (no obstacles in right range)
    #         # target = self.array_state[pos[0]][pos[1]+dist]
    #         try:
    #             target = self.array_state[pos[0]][pos[1]+dist]
    #             if(pos[1]+dist>9): return 0
    #         except:
    #             return 0
    #         if target == 0 and all(space == 0 for space in self.array_state[pos[0]][pos[1]+1:pos[1]+dist]):
    #             self.array_state[pos[0]][pos[1]+dist] = man
    #             self.array_state[pos[0]][pos[1]] = 0
    #             return 1
    #         return 0
        

    #     return 0
    
    def MisplacedTileHeuristic(self):
        cnt = 0
        if not self.array_state[1][0] == 1: cnt+=1
        if not self.array_state[1][1] == 2: cnt+=1
        if not self.array_state[1][2] == 3: cnt+=1
        if not self.array_state[1][3] == 4: cnt+=1
        if not self.array_state[1][4] == 5: cnt+=1
        if not self.array_state[1][5] == 6: cnt+=1
        if not self.array_state[1][6] == 7: cnt+=1
        if not self.array_state[1][7] == 8: cnt+=1
        if not self.array_state[1][8] == 9: cnt+=1
        return cnt

    def ManhattanDistanceHeuristic(self):
        dist = 0

        # # Find position of 1, sergeant
        # s_pos = self.getPosMan(1)
        # # find distance between pos and 1,0
        # dist = self.cost(1,s_pos)
        # for i in range(2, self.men+1):
        #     # MANHATTAN
        #     # pos = self.getPosMan(i)
        #     # dist+= abs(pos[0]-1)+abs(pos[1]-(i-1))
            
        #     # MISPLACED TILE
        #     pos = self.getPosMan(i)
        #     if pos[1]!=i-1 or pos[0]!=1:
        #         dist+=1
        # return dist

        man = 0
        m_pos = None
        for i in range(1,self.men+1):
            # Find position of i
            m_pos = self.getPosMan(i)
            man = i
            # find distance between pos and i
            # dist = abs(m_pos[0]-1)+abs(m_pos[1]-(i-1))
            if man==1: dist = self.cost(i,m_pos)
            else: dist = abs(m_pos[0]-1)+abs(m_pos[1]-(i-1))
            # print(dist)
            if (dist==0): continue # if the current man is already in position, its h(n)=0 so move on to the next
            break

        for j in range(man+1, self.men+1):
            # MISPLACED TILE of rest of men
            pos = self.getPosMan(j)
            if pos[1]!=j-1 or pos[0]!=1 or (m_pos[0]!=1 or m_pos[1]!=(man-1)):
                dist+=1
            if (self.array_state[0][3]==0 and pos[1]==3) and m_pos[1]>3 and not self.getManMoveRecess(man,m_pos, 3): dist+=1 
            elif (self.array_state[0][5]==0 and pos[1]==5) and m_pos[1]>5 and not self.getManMoveRecess(man,m_pos, 5): dist+=1
            elif (self.array_state[0][7]==0 and pos[1]==7) and m_pos[1]>7 and not self.getManMoveRecess(man,m_pos, 7): dist+=1

        return dist

    def cost(self, man, m_pos):
        cost = 0
        target = (man-1)
        if(m_pos[1]!=target): cost+=1
        if target<3 and m_pos[1]>3: cost+=1
        if target<5 and m_pos[1]>5: cost+=1
        if target<7 and m_pos[1]>7: cost+=1
        for i in range(man+1,self.men+1):
            pos = self.getPosMan(i)
            if pos[1] in range(target,m_pos[1]+1):
                cost+=1 # If this man is to the left of the sergeant, they need to move out of the way
            # If for each recess that is to the left of the sergeant, it is not filled or there are other men to the right, add 1

            # CODE 1
            # if (self.array_state[0][3]==0 and pos[1]>=3) and m_pos[1]>3 and not self.getManMoveRecess(man,m_pos, 3): cost+=1 
            # elif (self.array_state[0][5]==0 and pos[1]>=5) and m_pos[1]>5 and not self.getManMoveRecess(man,m_pos, 5): cost+=1
            # elif (self.array_state[0][7]==0 and pos[1]>=7) and m_pos[1]>7 and not self.getManMoveRecess(man,m_pos, 7): cost+=1
        return cost
    
    def getManMoveRecess(self, man, m_pos,recess):
        cnt=0
        # Check if possible to move man directly to recess
        if self.array_state[0][recess]==0 and all(space == 0 for space in self.array_state[1][recess:m_pos[1]]):
            return True
        return False

class NineMenTrench:
    operators = 3
    h_size = 10
    v_size = 2
    men = 0
    goal = None
    TrenchState = TrenchState()

    def InitialState(self):
        self.TrenchState.InitializeTrench(10, 9)
        self.men = self.TrenchState.men
        self.h_size = self.TrenchState.size
        
        self.goal = [[None for i in range(self.h_size)] for j in range(2)]
        other = True # every other spot is a recess in the top row, aside from 3 spaces in the front and 2 spaces in the back
        cnt = 1
        for row in range(0,2):
            for col in range(0,self.h_size):
                if row == 0 and col > 2 and col <= self.h_size-2 and other:
                    self.goal[row][col] = 0
                    other = False
                elif other==False:
                    other = True

                if row == 1 and col >= 0:
                    # initialize trench with men
                    if cnt <= self.men:
                        self.goal[row][col] = cnt
                        cnt+=1
                    else:
                        self.goal[row][col] = 0
        # for row in goal:
        #     print(row)
        return self.TrenchState
    
    def GoalTest(self, state):
        if self.goal==state.array_state:
            return True
        # if state.array_state[1][0]==1: return True
        # if state.array_state[0][3]==1: return True
        # if state.array_state[0][5]==1: return True
        # if state.array_state[1][0]==2 and state.array_state[1][1]==3 and state.array_state[0][3]==4 and state.array_state[1][2]==5 and state.array_state[1][3]==6 and state.array_state[1][4]==8 and state.array_state[1][5]==9 and state.array_state[0][5]==7: return True
        # if state.array_state[1][0]==2 and state.array_state[1][1]==3  and state.array_state[1][2]==5 and state.array_state[1][3]==0 and state.array_state[1][4]==0 and state.array_state[0][3]==1: return True

        # if (state.array_state[1][0] == 2 
        # and state.array_state[1][1] == 3
        # and state.array_state[1][2] == 5
        # and state.array_state[1][3] == 6
        # and state.array_state[1][4] == 8
        # and state.array_state[1][5] == 0
        # and state.array_state[1][6] == 0
        # and state.array_state[1][7] == 0
        # and state.array_state[1][8] == 7
        # and state.array_state[1][9] == 9
        # and state.array_state[0][3] == 4
        # and state.array_state[0][5] == 0
        # and state.array_state[0][7] == 1):
        #     return True

        # if (state.array_state[1][0]==2 
        #     and state.array_state[1][1]==3 
        #     and state.array_state[1][2]==5 
        #     and state.array_state[1][3]==6 
        #     and state.array_state[1][4]==8 
        #     and state.array_state[1][5]==9 
        #     and state.array_state[0][3]==4 
        #     and state.array_state[0][5]==7
        #     and state.array_state[0][7]==1
        #     ): return True
        return False
    
    # return array of nodes post operation
    # Attempt move a single man in direction dir, with dist # of spaces
        # dir = 0, move left, 9 possible spaces
        # dir = 1, move up or down, 1 possible space
        # dir = 2, move right 9 possible spaces
    # For each man, for each direction, for each valid distance, expand node to create new_node
    # Add new_node to node_arr, then continue
    def Operate(self, node):
        node_arr = []
        for man in range(1, self.men+1):
            for dir in range(0,3):
                match dir:
                    case 0:
                        for dist in range(1, self.h_size-1):
                            # If move is possible, do so and add to node_arr
                            # If not possible, means not enough space past that dist, so end loop early
                            new_node = copy.deepcopy(node)
                            if new_node.state.operate(man, dir, dist):
                                new_node.solution.append("MOVE "+str(man)+" in dir "+ str(dir)+ ": "+ str(dist)+ " spaces" )
                                node_arr.append(new_node)
                            else:
                                continue
                    
                    case 1:
                        for dist in range(0, 3):
                            # new_node = copy.deepcopy(node)
                            # if new_node.state.operate(man, dir, dist):
                            #     new_node.solution.append("MOVE "+str(man)+" in dir "+ str(dir)+ ": "+ str(dist)+ " spaces" )
                            #     node_arr.append(new_node)
                            # else:
                            #     continue
                            for h_dir in range(0,2):
                                for h_dist in range(0, self.h_size-1):
                                    # move horizontal then up
                                    if dist==0:
                                        new_node = copy.deepcopy(node)
                                        if h_dir==0:
                                            new_node.state.operate(man, 0, h_dist) # Move left
                                            new_node.solution.append("MOVE "+str(man)+" left "+ str(h_dist)+ " spaces then up" )
                                        elif h_dir==1:
                                            new_node.state.operate(man, 2, h_dist) # Move right
                                            new_node.solution.append("MOVE "+str(man)+" right "+ str(h_dist)+ " spaces then up" )
                                        if new_node.state.operate(man, dir, dist):
                                            node_arr.append(new_node)
                                        else:
                                            continue
                                    elif dist == 1:
                                        # move down then move horizontal then move up
                                        new_node = copy.deepcopy(node)
                                        if new_node.state.operate(man, dir, 1): #move down
                                            if h_dir==0:
                                                new_node.state.operate(man, 0, h_dist) # Move left
                                                if new_node.state.operate(man, dir, 0): # Move Up
                                                    new_node.solution.append("MOVE "+str(man)+" down then move left "+ str(h_dist)+ " spaces then move up" )
                                                else: continue
                                            elif h_dir==1:
                                                new_node.state.operate(man, 2, h_dist) # Move right
                                                if new_node.state.operate(man, dir, 0): # Move Up
                                                    new_node.solution.append("MOVE "+str(man)+" down then move right "+ str(h_dist)+ " spaces then move up" )
                                                else: continue
                                        else:
                                            continue
                                        node_arr.append(new_node)
                                    elif dist == 2:
                                        # move down then move horizontal
                                        new_node = copy.deepcopy(node)
                                        if new_node.state.operate(man, dir, 1):
                                            if h_dir==0:
                                                new_node.state.operate(man, 0, h_dist) # Move left
                                                new_node.solution.append("MOVE "+str(man)+" down then move left "+ str(h_dist)+ " spaces" )
                                            elif h_dir==1:
                                                new_node.state.operate(man, 2, h_dist) # Move right
                                                new_node.solution.append("MOVE "+str(man)+" down then move right "+ str(h_dist)+ " spaces" )
                                            node_arr.append(new_node)
                                        else:
                                            continue
                    case 2:
                        for dist in range(1, self.h_size-1):
                            new_node = copy.deepcopy(node)
                            if new_node.state.operate(man, dir, dist):
                                new_node.solution.append("MOVE "+str(man)+" in dir "+ str(dir)+ ": "+ str(dist)+ " spaces" )
                                node_arr.append(new_node)
                            else:
                                continue
        # print("---------------------------------------\n")
        return node_arr



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
    valid = False
    valid = test.operate(3,0,2)
    if valid:
        print("VALID", valid)
    else:
        print("INVALID?", valid)
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

def test2():
    test = TrenchState()
    test.InitializeTrench(10, 9)
    print("INITIAL STATE:")
    test.printState()
    
    for i in range(2,10):
        print("TEST: LEFT")
        test.operate(i,0,1)
        test.printState()

    print("\n")
    print("TEST: LEFT")
    test.operate(1,0,1)
    test.printState()

def test3():
    test = TrenchState()
    test.InitializeTrench(10, 9)
    print("INITIAL STATE:")
    test.printState()

    print("MH:", test.ManhattanDistanceHeuristic())

    print("\n")
    print("TEST: LEFT")
    test.operate(1,0,1)
    test.printState()

    print("\n")
    print("TEST: RIGHT")
    test.operate(1,2,1)
    test.printState()

def test4():
    test = TrenchState()
    test.InitializeTrench(10, 9)
    print("INITIAL STATE:")
    test.printState()

    print("MH:", test.ManhattanDistanceHeuristic())
# test()
# test2()
# test3()
# test4()