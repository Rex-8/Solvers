# What if there is a new agent 'Devil' added such that it can consume the wolf
# To accomodate the changes to the agents , lets also add an extra space in the boat

class State:
    def __init__(self, man, goat, cabbage, wolf, devil):
        self.man = man
        self.goat = goat
        self.cabbage = cabbage
        self.wolf = wolf
        self.devil = devil

    def is_valid(self):
        if (self.goat == self.cabbage and self.man != self.goat) or (self.goat == self.wolf and self.man != self.goat):return False
        if (self.wolf == self.devil and self.devil != self.man):return False
        return True

    def is_goal(self):
        return self.man == 1 and self.goat == 1 and self.cabbage == 1 and self.wolf == 1 and self.devil == 1

def get_possible_moves(state):
    moves = []
    moves.append(State(1 - state.man, state.goat, state.cabbage, state.wolf, state.devil))
    if state.goat == state.man: moves.append(State(1 - state.man, 1 - state.goat, state.cabbage, state.wolf, state.devil))
    if state.cabbage == state.man: moves.append(State(1 - state.man, state.goat, 1 - state.cabbage, state.wolf, state.devil))
    if state.wolf == state.man: moves.append(State(1 - state.man, state.goat, state.cabbage, 1 - state.wolf, state.devil))
    if state.devil == state.man: moves.append(State(1 - state.man, state.goat, state.cabbage, state.wolf, 1 - state.devil))
    return moves

def backtrack(state, path):
    if not state.is_valid():
        return False
    if state.is_goal():
        return path

    for next_state in get_possible_moves(state):
        if next_state not in path:
            result = backtrack(next_state, path + [next_state])
            if result:
                return result

    return False

initial_state = State(0, 0, 0, 0, 0)
solution = backtrack(initial_state, [initial_state])
    
if solution:
    for step in solution:
        print(f'Man: {step.man}, Goat: {step.goat}, Cabbage: {step.cabbage}, Wolf: {step.wolf}, Devil: {step.devil}')
else:
    print("Mission failed")