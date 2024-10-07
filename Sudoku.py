bd = [[5, 3, 0, 0, 7, 0, 0, 0, 0],[6, 0, 0, 1, 9, 5, 0, 0, 0],[0, 9, 8, 0, 0, 0, 0, 6, 0],[8, 0, 0, 0, 6, 0, 0, 0, 3],[4, 0, 0, 8, 0, 3, 0, 0, 1],[7, 0, 0, 0, 2, 0, 0, 0, 6],[0, 6, 0, 0, 0, 0, 2, 8, 0],[0, 0, 0, 4, 1, 9, 0, 0, 5],[0, 0, 0, 0, 8, 0, 0, 7, 9]]

## Trying to minimize lines to make life tough

def print_bd(bd): [print(row) for row in bd]
def has_multiple(grp): return bool([grp.count(ele)>1 for ele in range(1,10)].count(True)>0)
def is_valid(bd): return not True in ([has_multiple(row) for row in bd] + [has_multiple([bd[j][i] for j in range(9)]) for i in range(9)] + [has_multiple([bd[j][i] for j in range(y,y+3) for i in range(x,x+3)]) for y in range(0,9,3) for x in range(0,9,3)])
def solve_board(bd):
    for j in range(9):
        for i in range(9):
            if bd[j][i] == 0:
                for ele in range(1,10):
                    bd[j][i] = ele
                    if is_valid(bd):
                        if solve_board(bd):
                            return bd
                    bd[j][i] = 0
                return False
    return True

solve_board(bd)
print_bd(bd)