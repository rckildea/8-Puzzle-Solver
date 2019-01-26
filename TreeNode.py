"""
Author: Ryan Kildea
Date created: 01/25/19
Last modified: 01/26/19
"""


class TreeNode:
    """
    Structure for an 8-puzzle that allows for the creation of a tree with multiple branches.
    Keeps track of parent, children, puzzle string representation, and the previous move that led to the current state.
    """
    branches = []
    parent_node = None
    data = ""
    swapped_number = None

    def __init__(self, numbers):
        """
        :param numbers: String representation of the puzzle
        """
        self.data = numbers

    def add_branch(self, branch_node):
        """
        Inserts a branch into the current node and sets the new branch's parent
        :param branch_node: Child node containing the next state
        :return:
        """
        self.branches.append(branch_node)
        branch_node.parent_node = self