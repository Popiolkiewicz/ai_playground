# 1. Create two lists, L and L seen . At the beginning, L contains only the initial state, and L seen is
# empty.
# 2. Let n be the ﬁrst element of L. Compare this state with the ﬁnal state. If they are identical,
# stop with success.
# 3. Apply to n all available search operators, thus obtaining a set of new states. Discard those
# states that already exist in L seen . As for the rest, sort them by the evaluation function and
# place them at the front of L.
# 4. Transfer n from L into the list, L seen , of the states that have been investigated.
# 5. If L D ; , stop and report failure. Otherwise, go to 2.

# 0 1 2
# 3 4 5
# 6 7 8

# Search operators: to <- from
# 0 <- 1, 3
# 1 <- 0, 2, 4
# 2 <- 1, 5
# 3 <- 0, 4, 6
# 4 <- 1, 3, 5, 7
# 5 <- 2, 4, 8
# 6 <- 3, 7
# 7 <- 4, 6, 8
# 8 <- 5, 7

import math

class HillClimbingSlidingTiles:
    initialState = ''
    finalState = ''

    allSearchOperators = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
    emptyTile = '-'
    tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    states = []
    statesVisited = []
    movesCounter = 0
    maxMoves = 10000

    def __init__(self, initialState, finalState):
        self.initialState = initialState
        self.finalState = finalState
        self.states.append(initialState)

    def run(self):
        success = False
        while (not success) and self.movesCounter < self.maxMoves:
            success = self.search()
        if success:
            print(f'Succeeded, moves count: {self.movesCounter}')
        else:
            print(f'Failure after {self.movesCounter} moves. :(')

    def search(self):
        print('')
        print(f'Iteration no: {self.movesCounter + 1}')
        print(f'n: {self.initialState}')
        # print(f'states: {self.states}')
        # print(f'statesVisited: {self.statesVisited}')

        if self.initialState == self.finalState:
            return True

        self.movesCounter += 1

        emptyTileIndex = self.initialState.index(self.emptyTile)
        searchOperators = self.allSearchOperators[emptyTileIndex]

        # print(f'searchOperators: {searchOperators}')

        newStates = []
        for searchOperator in searchOperators:
            strInitialState = list(self.initialState)
            strInitialState[emptyTileIndex], strInitialState[searchOperator] = strInitialState[searchOperator], \
                                                                               strInitialState[emptyTileIndex]
            newState = "".join(strInitialState)

            if newState not in self.statesVisited:
                newStates.append(newState)
            # else:
            #     print(f'Already visited: {newState}')

        newStates.sort(key=lambda x: self.evaluate(x))
        newStates.extend(self.states)
        self.states = newStates
        self.states.remove(self.initialState)
        self.statesVisited.append(self.initialState)

        if not self.states:
            raise ValueError("No states left to check!")

        self.initialState = self.states[0]
        return False

    def evaluate(self, state):
        howFar = 0
        for tile in self.tiles:
            tileCurrentIndex = state.index(tile)
            tileFinalIndex = self.finalState.index(tile)
            higherIndex = max(tileCurrentIndex, tileFinalIndex)
            lowerIndex = min(tileCurrentIndex, tileFinalIndex)
            verticalDiff = math.floor(higherIndex / 3) - math.floor(lowerIndex / 3)
            horizontalDiff = abs(higherIndex % 3 - lowerIndex % 3)

            # print(tileCurrentIndex, tileFinalIndex, verticalDiff, '+', horizontalDiff)

            howFar += verticalDiff + horizontalDiff
        return howFar


# obj = HillClimbingSlidingTiles('A-EGBHDFC', 'ABCDEFGH-')
# obj = HillClimbingSlidingTiles('CFBDAGHE-', 'ABCDEFGH-')
obj = HillClimbingSlidingTiles('EACHDFGB-', 'ABCDEFGH-')
obj.run()
