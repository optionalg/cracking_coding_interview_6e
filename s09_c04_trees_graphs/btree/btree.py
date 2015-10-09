class Node(object):
    val = None
    left = None
    right = None

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def visit(node):
    print node.value


def in_order(node):
    if node is not None:
        in_order(node.left)
        visit(node.val)
        in_order(node.right)


def pre_order(node):
    if node is not None:
        visit(node.val)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        visit(node.val)
