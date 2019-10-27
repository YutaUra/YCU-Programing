from typing import Dict, Any, List

from Cell import Cell


class Group:
    def __init__(self, board, *index):
        self.index = set(index)
        self.filled = self.fetch(board)
        self.complete = False

    def get_cells(self, board):
        """
        :rtype: list[Cell]
        """
        cells = []
        for x, y in self.index:
            cells.append(board.board[y][x])
        return cells

    def fetch(self, board):
        cells = self.get_cells(board)
        filled_num = set(cell.number for cell in cells if cell.number)
        for cell in cells:
            if cell.not_allow(*filled_num):
                return self.fetch(board)
        return filled_num

    def update(self, board):
        filled = self.fetch(board)
        not_filled_cells = [cell for cell in self.get_cells(board) if not cell.number]
        prob: Dict[int, List[Cell]] = {n: [] for n in (set(i + 1 for i in range(9)) - filled)}
        for cell in not_filled_cells:
            for n in cell.allowed_num_set:
                prob[n].append(cell)
        # probから、一つの数字について、埋めることができる場所が1つしかないやつがあれば埋める。
        # 例えば、埋められる数字が、{1,8},{1,8},{1,8,4}だとすると、4は3番目で確定する
        # {1,2},{1,2},{1,2},{3,4} ⇒ エラー
        for key, value in prob.items():
            if len(value) == 1:
                if value[0].is_allowed(key):
                    value[0].number = key
                    filled.add(key)
                else:
                    raise Exception()
        if self.filled != filled:
            # 前回のupdateの呼び出しから、新しく埋まった数字があるので、再び更新する
            for cell in not_filled_cells:
                cell.not_allow(*filled)
            self.filled = filled
            self.update(board)

    def is_complete(self, board):
        if self.complete:
            return True
        cells = self.get_cells(board)
        for cell in cells:
            if not cell.number:
                return False
        self.complete = True
        return True

    def pattern(self, board):
        board.update_all()
        if self.is_complete(board):
            return list()
        not_filled_cells = [cell for cell in self.get_cells(board) if not cell.number]
        return self.make_pattern(not_filled_cells)

    def make_pattern(self, not_filled_cells: List[Cell], unused_number=None):
        unused_number = unused_number or set(i + 1 for i in range(9)) - self.filled
        not_filled_cells.sort(key=lambda x: len(x.allowed_num_set & unused_number))
        cell = not_filled_cells[0]

        if len(not_filled_cells) == 2:
            cell2: Cell = not_filled_cells[1]
            if len(cell.allowed_num_set & unused_number) == 1:
                num1 = list(cell.allowed_num_set & unused_number)[0]
                num2 = list(cell2.allowed_num_set - (cell.allowed_num_set & unused_number))[0]
                return [
                    [
                        [*cell.index, num1],
                        [*cell2.index, num2]
                    ]
                ]
            unused_number = list(unused_number)
            return [
                [
                    [*cell.index, unused_number[0]],
                    [*cell2.index, unused_number[1]],
                ], [
                    [*cell.index, unused_number[1]],
                    [*cell2.index, unused_number[0]],
                ]
            ]

        others = not_filled_cells[1:]
        return [
            [
                [*cell.index, n],
                *p
            ] for n in cell.allowed_num_set & unused_number
            for p in self.make_pattern(others, set(num for num in unused_number if num != n))
        ]
