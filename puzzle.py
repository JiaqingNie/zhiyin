import numpy as np
from copy import deepcopy

class Puzzle:
    def __init__(self, size=3):
        self.board = np.array([i + 1 for i in range(size * size)])
        self.board[size * size - 1] = 0
        self.size = size

        self.generate_random_board()
        self.move_blank_to_the_head()

        self.blank = 0

    def generate_random_board(self):
        np.random.shuffle(self.board)
        while self.count_inverse_number() % 2 != 0:
            np.random.shuffle(self.board)

    def move_blank_to_the_head(self):
        blank = np.where(self.board == 0)[0][0]
        for i in range(blank, 0, -1):
            self.board[i], self.board[i - 1] = self.board[i - 1], self.board[i]

    def count_inverse_number(self):
        s = 0
        size = self.size
        for i in range(size * size - 1):
            if self.board[i] != 0:
                for j in range(i + 1, size * size):
                    if self.board[j] != 0:
                        if self.board[i] > self.board[j]:
                            s += 1
        return s

    def _count_manhattan_distance(self):
        s = 0
        size = self.size
        for i in range(size * size):
            s += abs(self.board[i] - i)

        return s

    def calculate_utility(self):
        return - (self.count_inverse_number() + self._count_manhattan_distance())

    def snapshot(self):
        return tuple(self.board)

    def display(self):
        size = self.size
        state = self.snapshot()
        for i in range(len(state)):
            if state[i] != 0:
                print("%-2d" % (state[i]), end=" ")
            else:
                print("%-2s" % "#", end=" ")
            if (i + 1) % size == 0:
                print("")

    def win(self):
        return self._count_manhattan_distance() == 0

    def move_down(self):
        if self.blank >= self.size:
            other = self.blank - self.size
            self.board[other], self.board[self.blank] = self.board[self.blank], self.board[other]
            self.blank = other

    def move_up(self):
        if self.blank < self.size ** 2 - self.size:
            other = self.blank + self.size
            self.board[other], self.board[self.blank] = self.board[self.blank], self.board[other]
            self.blank = other

    def move_right(self):
        if self.blank % self.size != 0:
            other = self.blank - 1
            self.board[other], self.board[self.blank] = self.board[self.blank], self.board[other]
            self.blank = other

    def move_left(self):
        if self.blank % self.size != self.size - 1:
            other = self.blank + 1
            self.board[other], self.board[self.blank] = self.board[self.blank], self.board[other]
            self.blank = other

    def clone(self):
        res = Puzzle(self.size)
        res.board = deepcopy(self.board)
        res.blank = self.blank
        return res

