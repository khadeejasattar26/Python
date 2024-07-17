class Node:

#state = state # class variable shared by all instances

    def __init__(self, state, parent, actions, totalCost):

        self.state = state

        # instance variable unique to each instance

        self.parent = parent

        self.actions = actions 


        # only output states of those actions

        self.totalCost = totalCost
graph ={'A' : Node('A', None, ['B', 'E' , 'C'], None),

'B':  Node('A', None, ['B', 'E' , 'C'], None),

'C': Node('A', None, ['B', 'E' , 'C'], None),
'D': Node('A', None, ['B', 'E' , 'C'], None),
'E': Node('A', None, ['B', 'E' , 'C'], None),

'F':  Node('A', None, ['B', 'E' , 'C'], None),
'G':  Node('A', None, ['B', 'E' , 'C'], None)}