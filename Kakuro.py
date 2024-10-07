bd = [
    ['B', 'B', 'B', {'C': 21}, {'C': 16}, {'C': 20}, 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', {'R': 18, 'C': 15}, 0, 0, 0, 'B', 'B', 'B'],
    ['B', {'R': 10, 'C': 9}, 0, {'C': 7}, 0, 0, 0, 0, 0, 'B'],
    ['B', 0, 0, 0, {'R': 16, 'C': 12}, 0, 0, 0, 0, 'B'],
    ['B', 0, 0, {'C': 12}, 0, {'R': 17, 'C': 9}, 0, 0, 'B', 'B'],
    ['B', 0, {'R': 11, 'C': 11}, 0, 0, 0, {'R': 12, 'C': 9}, 0, 'B', 'B'],
    ['B', 0, 0, 0, {'C': 7}, 0, 0, {'R': 9, 'C': 6}, 0, 'B'],
    ['B', 0, 0, 0, 0, 0, 0, 0, 0, 'B'],
    ['B', 0, {'R': 9, 'C': 15}, 0, 0, {'R': 15, 'C': 12}, 0, 0, 0, 'B'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
]


if bd != [] : num_of_rows, num_of_cols = len(bd), len(bd[0])

def print_bd(bd):
    for row in bd:
        [print(col, end='       ') for col in row]
        print()

def get_lim(bd):
    bd_lim = [[r for r in col] for col in bd]
    for j in range(num_of_rows):
        for i in range(num_of_cols):
            if bd[j][i] == 0:
                r = 0
                for r1 in range(i - 1, -1, -1): 
                    if isinstance(bd[j][r1], dict):
                        r = bd[j][r1]['R']
                        break
                c = 0
                for c1 in range(j - 1, -1, -1):
                    if isinstance(bd[c1][i], dict):
                        c = bd[c1][i]['C']
                        break
                bd_lim[j][i] = min(r, c)
    return bd_lim

bd_lim = get_lim(bd)

def check_if_valid(bd):
    for j in range(num_of_rows):
        for i in range(num_of_cols):
            if isinstance(bd[j][i], dict):
                if 'R' in bd[j][i]:
                    row_sum = 0
                    empty_cells = 0
                    for r in range(i + 1, num_of_cols):
                        if bd[j][r] == 'B' or isinstance(bd[j][r], dict):
                            break
                        if bd[j][r] == 0:
                            empty_cells += 1
                        row_sum += bd[j][r]
                    if empty_cells == 0 and row_sum != bd[j][i]['R']:
                        return False
                    if row_sum > bd[j][i]['R']:
                        return False

                if 'C' in bd[j][i]:
                    col_sum = 0
                    empty_cells = 0
                    for c in range(j + 1, num_of_rows):
                        if bd[c][i] == 'B' or isinstance(bd[c][i], dict):
                            break
                        if bd[c][i] == 0:
                            empty_cells += 1
                        col_sum += bd[c][i]
                    if empty_cells == 0 and col_sum != bd[j][i]['C']:
                        return False
                    if col_sum > bd[j][i]['C']:
                        return False
    return True

def solve_board(bd):
    for j in range(num_of_rows):
        for i in range(num_of_cols):
            if bd[j][i] == 0:
                for ele in range(1, bd_lim[j][i] + 1):
                    bd[j][i] = ele
                    if check_if_valid(bd):
                        if solve_board(bd):
                            return bd
                    bd[j][i] = 0  
                return False
    return True  

solve_board(bd)
print("solved :")
print_bd(bd)
