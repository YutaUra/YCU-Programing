from Board import Board
from help import create_grid_by_str

test1 = '''
517  600  034
089  004  000
306  205  090

600  000  010
030  006  047
000  000  000

090  000  078
703  400  560
000  000  000
'''
test1 = create_grid_by_str(test1)

test2 = '''
530070000
600195000 
098000060
800060003
 400803001 
 700020006
060000280
 000419005
  000080079'''

b = Board(test1)
b.update_all()

b.show()
