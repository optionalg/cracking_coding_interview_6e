class Node(object):
    """
    An instance is a node in a graph.
    """
    val = None
    seen = False
    adj = None

    def __init__(self, val, seen, adj):
        self.val = val
        self.seen = seen
        self.adj = adj


class Lgraph(object):
    """
    An instance is a graph, implemented using adjacency lists.
    """
    nodes = []

    def __init__(self, nodes):
        self.nodes = nodes


def visit(node):
    """
    Define the operation for visiting a node.
    """
    print node.val


def dfs(node):
    """
    Perform depth-first search from a node.
    """
    if node is None:
        return
    visit(node)
    node.seen = True
    for each in node.adj:
        if not each.seen:
            dfs(each)


def bfs(node):
    """
    Perform breadth-first search from a node.
    """
    queue = []
    node.seen = True
    queue += node
    while queue:
        cur = queue.pop(0)
        visit(cur)
        for each in cur.adj:
            if not each.seen:
                each.seen = True
                queue += each
