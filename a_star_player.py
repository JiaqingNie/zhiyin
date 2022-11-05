from queue import PriorityQueue
from utils import PuzzleState


class AStarPlayer:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = puzzle.size

    def solve(self):
        visited = set()
        Q = PriorityQueue()
        puzzle_state = PuzzleState(self.puzzle)
        visited.add(puzzle_state.state)
        Q.put(puzzle_state)
        while not Q.empty():
            state = Q.get()
            puzzle = state.get_puzzle()
            if puzzle.win():
                ptr = state
                res = []
                while ptr:
                    res.append(ptr.move_from_parent)
                    ptr = ptr.parent
                return res[::-1]

            puzzle1 = state.get_puzzle()
            puzzle1.move_up()
            if puzzle1.snapshot() not in visited:
                visited.add(puzzle1.snapshot())
                Q.put(PuzzleState(puzzle1, state, "up"))

            puzzle2 = state.get_puzzle()
            puzzle2.move_down()
            if puzzle2.snapshot() not in visited:
                visited.add(puzzle2.snapshot())
                Q.put(PuzzleState(puzzle2, state, "down"))

            puzzle3 = state.get_puzzle()
            puzzle3.move_left()
            if puzzle3.snapshot() not in visited:
                visited.add(puzzle3.snapshot())
                Q.put(PuzzleState(puzzle3, state, "left"))

            puzzle4 = state.get_puzzle()
            puzzle4.move_right()
            if puzzle4.snapshot() not in visited:
                visited.add(puzzle4.snapshot())
                Q.put(PuzzleState(puzzle4, state, "right"))

        print("Unsovlable!")
        return []





