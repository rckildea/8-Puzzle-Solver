class tree_node:
    branches = []
    parent_node = None
    data = ""
    swapped_number = None

    def __init__(self, numbers):
        self.data = numbers

    def add_branch(self, branch_node):
        self.branches.append(branch_node)
        branch_node.parent_node = self