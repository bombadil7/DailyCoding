class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    node


def deserialize(string):
    """ The serialized string starts with root, followed by
    left and right sub-strings inside perinthesis, separated by a pipe |.
    Each substring if it has children has them enclosed inside perins.
    Examlpe: root(left(left.left|)|right)
    """
    return Node(string.split("(", 1)[0])


def main():
    #node = Node('root', Node('left', Node('left.left')), Node('right'))
    #assert deserialize(serialize(node)).left.left == 'left.left'
    deserialize("left{root}right")

if __name__ == "__main__":
    main()