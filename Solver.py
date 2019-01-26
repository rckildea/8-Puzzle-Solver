import queue
import TreeNode

"""
Author: Ryan Kildea
Date created: 01/25/19
Last modified: 01/26/19
"""


class Solver:
    """
    Finds solution (or discovers there is no solution) for a traditional 8-puzzle problem by implementing
    a Breadth-First search.  Keeps track of already visited states using a Set.
    """
    solved_puzzle = "12345678E"

    def __init__(self, puzzle, puzzle_number):
        """
        :param puzzle: 1D List representation of the current puzzle
        :param puzzle_number: Current puzzle number
        """
        self.visited_set = set()  # Keeps track of states already processed
        self.q = queue.Queue()
        self.solver_tree = None
        self.puzzle = puzzle
        self.puzzle_number = puzzle_number

    def solve(self):
        """
        Using a Breadth-First Search, finds the solution of an 8-puzzle, or discovers there is no solution.
        :return: None
        """
        solver_tree = TreeNode.TreeNode(
            "".join(self.puzzle))  # Tracks all solution attempts to trace solution path
        self.q.put(solver_tree)

        while True:
            if self.q.empty(): # No more possible states
                print("No solution for puzzle number {}".format(self.puzzle_number))
                break

            self.solver_tree = self.q.get()

            if self.solver_tree.data == Solver.solved_puzzle:
                self.handle_solved_puzzle()
                break

            empty_index = self.solver_tree.data.index("E")
            self.puzzle = list(self.solver_tree.data)
            string_representation = self.solver_tree.data
            self.visited_set.add(string_representation)

            legal_moves = Solver.get_legal_moves(empty_index)

            for move in legal_moves:
                self.process_move(move, empty_index)

    @staticmethod
    def get_legal_moves(e_location):
        """
        Finds all legal moves for a given state.  Using this 8-puzzle representation:

        0 | 1 | 2
        ----------
        3 | 4 | 5
        ----------
        6 | 7 | 8

        The empty space determines what moves are possible.  So, if the empty space is located at '0',
        the possible moves are to move '1' or to move '3'.  Thus, 0: [1, 3].

        :param e_location: Index of the board with the empty space
        :return: Array containing moves
        """
        return {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }.get(e_location)

    def process_move(self, move, empty_index):
        """
        Creates a board representations for the next move, and if this is a new, unique state, adds it to the solver queue.

        :param move: The index of the item to switch with the empty space
        :param empty_index: The index of the empty space
        :return: None
        """
        swap_puzzle = self.puzzle.copy()
        swap_puzzle[empty_index], swap_puzzle[move] = swap_puzzle[move], swap_puzzle[empty_index] # Move the selected tile to the empty spot
        swap_string_representation = "".join(swap_puzzle)

        if swap_string_representation not in self.visited_set: # Do not return to previously visited states
            new_branch = TreeNode.TreeNode(swap_string_representation)
            new_branch.swapped_number = swap_puzzle[empty_index]
            self.solver_tree.add_branch(new_branch)
            self.q.put(new_branch)

    def handle_solved_puzzle(self):
        """
        Once a puzzle is solved, traces back up the move tree, keeping track of all items moved.
        Then, prints these moves in order for the user to follow.
        :return: None
        """
        solution_steps = []
        print("Solved puzzle number {}.  Steps:".format(self.puzzle_number))

        while self.solver_tree.parent_node:
            solution_steps.append(self.solver_tree.swapped_number)
            self.solver_tree = self.solver_tree.parent_node

        solution_steps.reverse()  # Tree traversed bottom-up; reversed to get correct order

        for step in solution_steps:
            print("Move {item}".format(item=step))