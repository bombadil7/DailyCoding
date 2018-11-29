""" Node does not create a real binary tree, it doesn't care what values
    it puts in for left and right, but that is how it is specified 
    in the problem statement.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    """ serialize keeps calling itself recursively until the 
        specified root runs out of children.
    """
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


def deserialize(string):
    """ The serialized string starts with root, followed by
    left and right sub-strings inside perintheses, separated by a pipe |.
    Each substring if it has children has them enclosed inside perins also.
    Examlpe: root(left(left.left|)|right)

    The function works recursively going deeper and deeper into children
    higherarchy until it finds the leaf (simple string with no children), or
    an empty child.  Then it returns with a node, which will be used to 
    assemble the parent.
    """
    # For empty string return None, which makes the logic simpler
    # at node creation
    if len(string) == 0:
        return None 

    # Simplest case - leaf, no children
    if string.count("(") == 0:
        return Node(string)

    # Extract parent and children
    subs = string.split("(", 1)
    root = subs[0]
    # Remove closing bracket
    rest = subs[1][:-1]

    # Simple case - left child has no children
    left, right = rest.split("|", 1)
    if left.count("(") == 0:
        return Node(root, deserialize(left), deserialize(right))

    # Keep moving right until we find the end of left's children
    next_index = rest.index("|", len(left)+1)
    left = rest[:next_index]
    right = rest[next_index+1:]
    while left.count('(') != left.count(')'):
        next_index = rest.index("|", next_index+1)
        left = rest[:next_index]
        right = rest[next_index+1:]

    return Node(root, deserialize(left), deserialize(right))
    


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    node2 = Node('root', Node('left', Node('left.left', Node('left.left.left'), Node('right'))), Node('right', Node('left'), Node('right')))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    #deserialize(r"root(left|right(|right))")
    #print(serialize(deserialize(r"root(left|right(|right))")))
    #deserialize(r"root(left(left.left|)|right(|right))")
    #print(serialize(deserialize(r"root(left(left(left|)|)|right(left|right(|right(|right))))")))
    print(serialize(deserialize(serialize(node2))))

if __name__ == "__main__":
    main()