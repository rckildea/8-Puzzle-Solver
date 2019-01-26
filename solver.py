import queue
import tree_node

def main():
    text = get_formatted_file("prog1_input.txt")

    total_puzzles = int(text[0]) # Number of puzzles contained in text file
    current_puzzle_number = 1
    current_puzzle = get_current_puzzle(text, current_puzzle_number)
    solved_puzzle = "12345678E"

    visited_set = set() # Keeps track of states already processed

    solver_tree = tree_node.tree_node("".join(current_puzzle)) # Tracks all solution attempts to trace solution path

    q = queue.Queue()

    q.put(solver_tree)

    while current_puzzle_number <= total_puzzles:
        while True:
            if q.empty(): # No more possible states
                print("Could not solve puzzle number {}".format(current_puzzle_number))
                break

            solver_tree = q.get()

            if solver_tree.data == solved_puzzle:
                print("Solved puzzle number {}.  Steps:".format(current_puzzle_number))
                solution_steps = []
                while not solver_tree.parent_node == None:
                    solution_steps.append(solver_tree.swapped_number)
                    solver_tree = solver_tree.parent_node
                solution_steps.reverse() # Tree traversed bottom-up; reversed to get correct order
                for step in solution_steps:
                    print("Move {item}".format(item=step))
                break

            empty_index = solver_tree.data.index("E")

            current_puzzle = list(solver_tree.data)

            string_representation = solver_tree.data
            visited_set.add(string_representation)

            legal_moves = get_legal_moves(empty_index)

            for move in legal_moves:
                swap_puzzle = current_puzzle.copy()
                swap_puzzle[empty_index], swap_puzzle[move] = swap_puzzle[move], swap_puzzle[empty_index]
                swap_string_representation = "".join(swap_puzzle)

                if swap_string_representation not in visited_set:
                    new_branch = tree_node.tree_node(swap_string_representation)
                    new_branch.swapped_number = swap_puzzle[empty_index]
                    solver_tree.add_branch(new_branch)
                    q.put(new_branch)

        visited_set.clear()
        current_puzzle_number += 1
        current_puzzle = get_current_puzzle(text, current_puzzle_number)
        solver_tree = tree_node.tree_node("".join(current_puzzle))
        q.put(solver_tree)


def get_formatted_file(file_name):
    test_file = open(file_name, "r")
    text = []

    for line in test_file:
        text.append(line.rstrip())

    return text


def get_current_puzzle(text, current_number):
    puzzle = []

    index = (current_number - 1) * 4 + 1

    if index+2 <= len(text):
        for line in range(index, index + 3):
            numbers = text[line].split(" ")
            for num in numbers:
                puzzle.append(num)

        return puzzle
    else:
        return []


def get_legal_moves(e_location):

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

if __name__ == '__main__':
    main()

'''
LEGAL MOVES
012
345
678

0: 1, 3
1: 0, 2, 4
2: 1, 5
3: 0, 4, 6
4: 1, 3, 5, 7
5: 2, 4, 8
6: 3, 7
7: 4, 6, 8
8: 5, 7
'''