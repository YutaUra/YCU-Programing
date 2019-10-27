from typing import List

from Cell import Cell
from Group import Group


class Board:
    board: List[List[Cell]]

    def __init__(self, _2d_cell):
        """
        :type _2d_cell: list[list[int]]
        """
        self.solution = set()
        if len(_2d_cell) != 9:
            raise Exception('_2d_cellの行数が9ではありません')
        self.board = []
        for index_y, cells in enumerate(_2d_cell):
            if len(cells) != 9:
                raise Exception('_2d_cellの中身が9個ではないものが含まれています')
            self.board.append([])
            for index_x, cell in enumerate(cells):
                if cell:
                    self.board[-1].append(Cell(index_x, index_y, cell))
                else:
                    self.board[-1].append(Cell(index_x, index_y))
        self.filled = self.count_filled()

        self.col = [Group(self, *[(x, y) for x in range(9)]) for y in range(9)]
        self.row = [Group(self, *[(x, y) for y in range(9)]) for x in range(9)]
        self.block = [Group(self, *[(l // 3 + b // 3 * 3, l % 3 + b % 3 * 3) for l in range(9)]) for b in range(9)]

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return str(self.board) == str(other.board)

    def count_filled(self):
        return len([cell for cells in self.board for cell in cells if cell.number])

    def update_all(self):
        for i in range(9):
            self.col[i].update(self)
            self.row[i].update(self)
            self.block[i].update(self)
        filled = self.count_filled()
        if filled != self.filled:
            self.filled = filled
            self.update_all()

    def create_new(self):
        """
        :rtype :Board
        """
        new_board_cells = [[cell.number for cell in cells] for cells in self.board]
        board = Board(new_board_cells)
        return board

    def show(self):
        for i, cells in enumerate(self.board):
            print('[', end='')
            for j, cell in enumerate(cells):
                print(cell.number or 'N', end=',')
                if j % 3 == 2:
                    print('  ', end='')
            print('],')
            if i % 3 == 2:
                print()

    def get_minimum_pattern(self):
        self.update_all()
        row_pattern = sum([row.pattern(self) for row in self.row], [])
        col_pattern = sum([col.pattern(self) for col in self.col], [])
        block_pattern = sum([block.pattern(self) for block in self.block], [])
        return min(row_pattern, col_pattern, block_pattern, key=lambda x: len(x))

    def solve(self, solution=None):
        """
        :type solution:set
        """
        self.update_all()
        if self.count_filled() == 9 * 9:
            if solution:
                solution.add(self)
            else:
                self.solution.add(self)
            return
        pattern = self.get_minimum_pattern()
        for case in pattern:
            new_board = self.create_new()
            for (x, y, number) in case:
                if new_board.board[y][x].is_allowed(number):
                    new_board.board[y][x].number = number
                else:
                    break
            else:
                try:
                    new_board.update_all()
                except Exception as e:
                    continue
                if new_board.count_filled() == 9 * 9:
                    if solution:
                        solution.add(new_board)
                    else:
                        self.solution.add(new_board)
                else:
                    if solution:
                        new_board.solve(solution)
                    else:
                        new_board.solve(self.solution)
            continue
