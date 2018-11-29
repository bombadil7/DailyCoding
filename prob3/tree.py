class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    serial = node.val 

    if node.left or node.right:
        serial += r'('

        if node.left:
            serial += serialize(node.left)
            
        serial += r'|' 
            
        if node.right:
            serial += serialize(node.right)
            
        serial += r')'

    return serial


def getlr(string):
    return Node('left'), Node('right')


def deserialize(string):
    """ The serialized string starts with root, followed by
    left and right sub-strings inside perinthesis, separated by a pipe |.
    Each substring if it has children has them enclosed inside perins.
    Examlpe: root(left(left.left|)|right)
    """
    #if len(string.split("(")) == 1:
    #    return Node(string)
    if string.count("(") == 0:
        return Node(string)

    #left, right = getlr(string)
    #if left:

    subs = string.split("(", 1)
    root = subs[0]
    rest = subs[1].rstrip(")")
    #print(root + " " + rest)
    #left, right = rest.split("|", 1)
    #if left 
    #return Node(root, )



    # Otherwise deserialize left, then deser right, return Node of the results
    # first find left and right
    # have to count perins to determine which pipe to split on from the left
    # from the right


    #return Node(string.split("(", 1)[0])


def main():
    #node = Node('root', Node('left', Node('left.left')), Node('right'))
    node = Node('root', Node('left', Node('left.left', Node('left.left.left'), Node('right'))), Node('right', Node('left'), Node('right')))
    #assert deserialize(serialize(node)).left.left == 'left.left'
    #print(serialize(deserialize(serialize(Node('root')))))
    print(serialize(node))
    deserialize(r"root(left|right(|right))")
    #print(serialize(deserialize(r"root(left|right(|right))")))

if __name__ == "__main__":
    main()