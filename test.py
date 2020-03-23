# 根据维基百科的文章：“生命游戏，也简称为生命，是由英国数学家约翰·霍顿·康威（John Horton Conway）于1970年设计的细胞自动机。”

# 给定一个具有m x n个单元的矩阵，每个单元的初始状态为 有生命（1）或 无生命（0）。每个单元格使用以下四个规则（取自以上Wikipedia文章）与其八个邻居（水平，垂直，对角线）进行交互：

# 1:
# 任何具有少于两个活邻居的活细胞都会死亡，由于人口不足造成的。1 -> 0
# 任何有两个或三个活邻居的活细胞都可以存活到下一代。 1 -> 1
# 任何具有三个以上活邻居的活细胞都将死亡，就像是人口过多。1 -> 0

# 0:
# 具有正好三个活邻居的任何死细胞都将变成活细胞，就像通过繁殖一样。 0 -> 1


# 给定当前状态，编写一个函数以计算板的下一个状态（一次更新后）。通过将上述规则同时应用于当前状态下的每个单元来创建下一个状态，在该状态下，生与死同时发生。

# 例：

# 输入：
# [
#   [0,1,0]，
#   [0,0,1]，
#   [1,1,1]，
(i, j)
for w in range(-1, 2):
    for v in range(-1, 2):
        if w == 0 and v == 0:
            continue

        new_i = i + w
        new_j = j + v


#   [0,0,0]
# ]
# 输出：
# [
#   [0,0,0]，
#   [1,0,1]，
#   [0,1,1]，
#   [0,1,0]
# ]

def gameOfLife(board):
    def _1_to_0():
        return 0

    return []


def get_circle(board):
    # 先想思路
    # 1. 先把每个元素遍历出来
    # 2. 找到每个元素周围的8个元素
    #
    pass
    length_row = len(board)
    length_column = len(board[0])
    new_matrix = [[0] * len(board) for _ in range(len(board[0]))]
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            lives = 0

            def is_pos_alive(arr):
                for pos in arr:
                    if pos[0] < 0 or pos[0] > m or pos[1] < 0 or pos[1] > n:
                        continue
                    if arr[pos[0]][pos[1]] == 1:
                        return True
                    return False

            l = [board[:i][:j], board[:i][j], board[:i][j:],
                 board[i][:j], board[i][j:],
                 board[i:][:j], board[i:][j], board[i:][j:],
                 ]
            for quyu in l:
                is_pos_alives(item)

            if board[i][j] == 0：
            if lives == 3:
                # 具有正好三个活邻居的任何死细胞都将变成活细胞，就像通过繁殖一样。 0 -> 1
                new_matrix[i][j] = 1
            else:
                new_matrix[i][j] = 0
        elif board[i][j] == 1:
        # 任何具有少于两个活邻居的活细胞都会死亡，由于人口不足造成的。1 -> 0
        if lives <= 2:
            new_matrix[i][j] == 0
        # 任何有两个或三个活邻居的活细胞都可以存活到下一代。 1 -> 1
        elif lives in [2, 3]:
            new_matrix[i][j] == 1
        # 任何具有三个以上活邻居的活细胞都将死亡，就像是人口过多。1 -> 0
        elif lives > 3:
            new_matrix[i][j] == 0


first_row = board[0]
last_row = board[-1]
first_column = [row[0] for row in board]
last_column = [row[-1] for row in board]

for pos in []:
    if pos[0] < 0 or pos[0] > m or pos[1] < 0 or pos[1] > n:
        continue
    if board[pos[0]][pos[1]] == 1:
        lives += 1

m = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
print(m)
get_circle(m)


import queue
q = queue.LifoQueue
pq = queue.PriorityQueue

import string
l = 'We are happy.'
l.replace(' ', '%20')
l.count(' ')

