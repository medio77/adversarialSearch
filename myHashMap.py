from treelib import Node, Tree


def hashmap(board):
    hashedString = ""
    for i in board:
        if board[i] == 1:
            hashedString += "r"
        elif (board[i] == -1):
            hashedString += "b"
        elif (board[i] == "e"):
            hashedString += "e"
    return hashedString


def dictToTree(tree,child_dict,parent_dict):
    tree.create_node(identifier=hashmap(child_dict), parent=hashmap(parent_dict))

def nodeToDict(tree,hashed_node):
    pass