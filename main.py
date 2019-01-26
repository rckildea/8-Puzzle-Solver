import Solver

"""
Author: Ryan Kildea
Date created: 01/25/19
Last modified: 01/26/19
"""


def main():
    """
    Reads in a traditional 8-puzzle from a text file and uses a Solver class to find a solution.
    """
    file_name = "prog1_input.txt"
    text = get_formatted_file(file_name)

    total_puzzles = int(text[0])  # Number of puzzles contained in text file
    current_puzzle_number = 1

    while current_puzzle_number <= total_puzzles:
        current_puzzle = get_current_puzzle(text, current_puzzle_number)
        puzzle_solver = Solver.Solver(current_puzzle, current_puzzle_number)
        puzzle_solver.solve()
        current_puzzle_number += 1


def get_formatted_file(file_name):
    """
    Reads in a text document and gets rid of trailing whitespace
    :param file_name: Name of text file
    :return: Formatted list of lines
    """
    test_file = open(file_name, "r")
    text = []

    for line in test_file:
        text.append(line.rstrip())

    return text


def get_current_puzzle(text, current_number):
    """
    Using the current puzzle number, locates and returns the next puzzle.
    :param text: List of formatted lines from original text document
    :param current_number: Current puzzle number
    :return: Formatted list containing the current puzzle
    """
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


if __name__ == '__main__':
    main()
