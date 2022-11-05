from puzzle import Puzzle


class PuzzleState:
    def __init__(self, puzzle, parent=None, move_from_parent=None):
        self.state = puzzle.snapshot()
        self.utility = puzzle.calculate_utility()
        self.size = puzzle.size
        self.parent = parent
        self.move_from_parent = move_from_parent

    def __lt__(self, other):
        return self.utility > other.utility

    def get_puzzle(self):
        puzzle = Puzzle(self.size)
        puzzle.board = list(self.state)
        puzzle.blank = puzzle.board.index(0)
        return puzzle
