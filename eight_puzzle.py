from simpleai.search import \
    (SearchProblem,
     breadth_first,
     depth_first,
     iterative_limited_depth_first,
     uniform_cost)
from simpleai.search.viewers import WebViewer, BaseViewer

initial_state = ((7, 3, 4),
                 (6, 8, 5),
                 (1, 2, 0))

goal_state = ((0, 1, 2),
              (3, 4, 5),
              (6, 7, 8))


def find_position_of_number(number, current_state):
    for row_index, row in enumerate(current_state):
        for column_index, column in enumerate(row):
            if column == number:
                return row_index, column_index


class EightPuzzle(SearchProblem):

    def is_goal(self, current_state):
        return current_state == goal_state

    def actions(self, current_state):
        possible_states = []
        zero_row, zero_column = find_position_of_number(0, current_state)
        if zero_row > 0:
            possible_states.append(current_state[zero_row - 1][zero_column])  # move zero up
        if zero_row < 0:
            possible_states.append(current_state[zero_row + 1][zero_column])  # move zero down
        if zero_column > 0:
            possible_states.append(current_state[zero_row][zero_column - 1])  # move zero left
        if zero_column < 0:
            possible_states.append(current_state[zero_row][zero_column + 1])  # move zero right
        # returns a list of possible values the next state can take
        return possible_states

    def result(self, current_state, action_to_do):
        zero_row, zero_column = find_position_of_number(0, current_state)
        number_to_move_row, number_to_move_column = find_position_of_number(action_to_do, current_state)
        # convert tuple to list
        # new_current_state = list(state)
        new_current_state = list(list(row) for row in current_state)
        # modify new_current_state
        new_current_state[number_to_move_row][number_to_move_column] = 0
        new_current_state[zero_row][zero_column] = action_to_do
        # convert list to tuple
        # new_current_state = tuple(new_current_state)
        new_current_state = tuple(tuple(row) for row in new_current_state)
        # returns a new state (new_current_state)
        return new_current_state

    def cost(self, current_state, action_to_do, resultant_state):
        return 1


# print(breadth_first(EightPuzzle(initial_state), graph_search=True, viewer=BaseViewer()).state)

methods = (
    breadth_first,
    depth_first,
    # iterative_limited_depth_first,
    uniform_cost,
)

# problem = EightPuzzle(initial_state)
# result = methods[0](problem, graph_search=True, viewer=WebViewer())

print('Initial State', initial_state)
print()
print('Goal State', goal_state)

for method in methods:
    print()
    print('=' * 50)

    print('Method:', method)
    visor = BaseViewer()
    problem = EightPuzzle(initial_state)
    result = method(problem, graph_search=False, viewer=visor)

    print('Final State:')
    print(result.state)

    print('-' * 50)

    for action, state in result.path():
        print('Action: ', action)
        print('Resultant State: ', state)

    print('Statistics:')
    print('Number of actions:', len(result.path()))
    print(visor.stats)
