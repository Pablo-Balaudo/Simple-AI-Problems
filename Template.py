from simpleai.search import \
    (SearchProblem,
     breadth_first,
     depth_first,
     iterative_limited_depth_first,
     uniform_cost)
from simpleai.search.viewers import WebViewer, BaseViewer

initial_state = ()

goal_state = ()


class NameOfTheProblem(SearchProblem):

    def is_goal(self, current_state):
        return current_state == goal_state

    def actions(self, current_state):
        possible_values = []
        # returns a list of possible values the next state1 can take
        return possible_values

    def result(self, current_state, action_to_do):
        # convert tuple to list
        # new_current_state = list(current_state)
        # modify new_current_state
        # convert list to tuple
        # new_current_state = tuple(new_current_state)
        # returns a new state (new_current_state)
        return None

    def cost(self, current_state, action_to_do, resultant_state):
        return 1


methods = (
    breadth_first,
    depth_first,
    iterative_limited_depth_first,
    uniform_cost,
)

problem = NameOfTheProblem(initial_state)
# result = methods[0](problem, graph_search=True, viewer=WebViewer())

print('Initial State ', initial_state)
print()
print('Goal State ', goal_state)

for method in methods:
    print()
    print('=' * 50)

    print('Method: ', method)
    visor = BaseViewer()
    problem = NameOfTheProblem(initial_state)
    result = method(problem, graph_search=True, viewer=visor)

    print('Final State: ')
    print(result.state)

    print('-' * 50)

    for action, state in result.path():
        print('Action: ', action)
        print()
        print('Resultant State: ', state)

    print()
    print('Statistics: ')
    print('Number of actions: ', len(result.path()))
    print(visor.stats)

