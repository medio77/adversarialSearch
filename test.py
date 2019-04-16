from treelib import Node,Tree



board = {0: '1', 1: '2', 2: '3',
         3: '4', 4: '5', 5: '6',
         6: '7', 7: '8', 8: '9'}
board2 = {0: '3', 1: '2', 2: '3',
         3: '4', 4: '1', 5: '6',
         6: '7', 7: '8', 8: '9'}
state = {0: 'e', 1: 'e', 2: 'e',
         3: 'e', 4: 'e', 5: 'e',
         6: 'e', 7: 'e', 8: 'e'}


def myhash(board):
    hashedString=""
    for i in board:
        if board[i]=='1':
            hashedString+="r"
        elif(board[i]=="-1"):
            hashedString+="b"
        elif(board[i]=="e"):
            hashedString+="e"
    return hashedString
print(myhash(state))


