import copy
# from anytree import Node,RenderTree
from treelib import Node, Tree

import myHashMap

state = {0: 'e', 1: 'e', 2: 'e',
         3: 'e', 4: 'e', 5: 'e',
         6: 'e', 7: 'e', 8: 'e'}
# triples = {0: [[1, 2], [3, 6], [4, 8]],
#            1: [[0, 2], [4, 7]],
#            2: [[0, 1], [5, 8], [4, 6]],
#            3: [[0, 6], [4, 5]],
#            4: [[1, 7], [3, 5], [0, 8], [2, 6]],
#            5: [[2, 8], [3, 4]],
#            6: [[0, 3], [7, 8], [2, 4]],
#            7: [[1, 4], [6, 8]],
#            8: [[2, 5], [6, 7], [0, 4]]}
triples = {0: [[0, 1, 2], [0, 3, 6], [0, 4, 8]],
           1: [[0, 1, 2], [1, 4, 7]],
           2: [[0, 1, 2], [2, 5, 8], [2, 4, 6]],
           3: [[0, 3, 6], [3, 4, 5]],
           4: [[1, 4, 7], [3, 4, 5], [0, 4, 8], [2, 4, 6]],
           5: [[2, 5, 8], [3, 4, 5]],
           6: [[0, 3, 6], [6, 7, 8], [2, 4, 6]],
           7: [[1, 4, 7], [6, 7, 8]],
           8: [[2, 5, 8], [6, 7, 8], [0, 4, 8]]}
triples_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
global counter, visited_list
visited_list = []
counter = 0


def tripled(board_tripled):
    for triple in triples_list:
        if board_tripled[triple[0]] == board_tripled[triple[1]] == board_tripled[triple[2]] and board_tripled[
            triple[2]] != 'e':
            return True
    return False


def openTriples(board_open):
    r_open_count = 0
    b_open_count = 0
    for triple in triples_list:
        if board_open[triple[0]] in ['e', 1] and board_open[triple[1]] in ['e', 1] and board_open[triple[2]] in ['e',
                                                                                                                 1]:
            r_open_count += 1
    for triple in triples_list:
        if board_open[triple[0]] in ['e', -1] and board_open[triple[1]] in ['e', -1] and board_open[triple[2]] in ['e',
                                                                                                                   -1]:
            b_open_count += 1

    return r_open_count - b_open_count


def rotate_cw(board):
    board[1], board[5], board[7], board[3] = board[3], board[1], board[5], board[7]
    board[0], board[2], board[8], board[6] = board[6], board[0], board[2], board[8]


def myhash(board):
    hashedString = ""
    for i in board:
        if board[i] == 1:   # turn 1 means red player's turn
            hashedString += "r"
        elif (board[i] == -1):
            hashedString += "b"
        elif (board[i] == "e"):
            hashedString += "e"
    return hashedString


def print_game(board):
    print_board = []
    shape = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in board:
        shape[i] = board[i]
    counter = 1
    for i in range(0, 9):
        if counter == 3:
            print(shape[i])
            counter = 0
        else:
            print(shape[i], end=""),
        counter += 1


def visited(board):
    global visited_list
    if board not in visited_list:
        visited_list.append(board)
        rotate_cw(board)
        visited_list.append(board)
        rotate_cw(board)
        visited_list.append(board)
        rotate_cw(board)
        visited_list.append(board)
        return False
    else:
        return True


def state_func(board, turn):
    if (not tripled(board)):
        # if (tripled(board)):
        #     if turn==1:
        #         tree.get_node(myhash(board)).data="plus"
        #     else:
        #         tree.get_node(myhash(board)).data="minus"
        global counter
        print(counter)
        counter += 1
        available_choices = []
        for i in board:
            if board[i] == 'e':
                available_choices.append(i)
        for choice in available_choices:
            child_board = copy.deepcopy(board)
            child_board[choice] = turn
            try:
                myHashMap.dictToTree(tree, child_board, board)
                state_func(child_board, -1 * turn)
            except:
                pass

        # backtracking happens in this line
        if tree.get_node(myhash(board)).is_leaf():  # to set heuristic when its leaf and choose when not leaf
            tree.get_node(myhash(board)).data = openTriples(board)
        else:
            if turn == 1:  # r player wants to maximize and b player wants to minimize
                for child in Tree.children(tree.get_node(myhash((board)))):
                    if child.data=="plus":
                        tree.get_node(myhash(board)).data="plus"
                    else:
                        pass
            elif turn == -1:
                pass
        # print("this is leaf with depth ",tree.depth(tree.get_node(myhash(board))))
    else:
        print("its tripled!!")
        if (tripled(board)):
            if turn == 1:
                tree.get_node(myhash(board)).data = "plus"
            else:
                tree.get_node(myhash(board)).data = "minus"


tree = Tree()
tree.create_node(identifier=myhash(state))
state_func(state, 1)  # r player starts the game

tree.show()
