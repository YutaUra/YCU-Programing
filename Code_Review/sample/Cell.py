class Cell:
    def __init__(self, index_x, index_y, number=None):
        self.__number = number
        self.__x = index_x
        self.__y = index_y
        if self.__number:
            self.__allowed = {number}
        else:
            self.__allowed = set(i + 1 for i in range(9))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def index(self):
        return self.__x, self.__y

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number in self.__allowed:
            self.__number = number
            self.__allowed = {number}
        else:
            print(f'{number=}\n {self.__allowed=}')
            print(self.index, self.number)
            raise Exception('Cellに収容不可能な値がセットされました。')

    @property
    def allowed_num_set(self):
        return self.__allowed

    def not_allow(self, *nums):
        if self.number:
            return
        self.__allowed -= set(nums)
        if len(self.__allowed) == 1:
            self.number = list(self.__allowed)[0]
            return True
        elif len(self.__allowed) == 0:
            raise Exception('Cellに収容可能な数字がなくなりました。')

    def is_allowed(self, num):
        return num in self.__allowed

    def __str__(self):
        return f'<Cell {self.number if self.number else "N"}>'

    def __repr__(self):
        return f'Cell({self.number})'
