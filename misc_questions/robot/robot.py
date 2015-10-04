"""
Calculate the number of unique paths a robot can take from the top left corner
to the bottom right corner of an n x n matrix.

Preconditions:

    Allow moves in all directions (up, down, left, right) at any point.
    Paths cannot cross themselves.
    Paths stay within the bounds of the matrix.

Authors:
    Kevin Schaich   (krs252@cornell.edu)
    Ian Lyons       (ian@blendlabs.com)
"""


def neighbors(pos_x, pos_y, n):
    """
    Return the visitable nodes directly adjacent to a position
    [pos_x] and [pos_y] on a matrix of dimensions [n] x [n].
    """
    neighbors = []

    top = (pos_x, pos_y - 1)
    bottom = (pos_x, pos_y + 1)
    left = (pos_x - 1, pos_y)
    right = (pos_x + 1, pos_y)

    if top[1] >= 0:
        neighbors.append(top)
    if bottom[1] < n:
        neighbors.append(bottom)
    if left[0] >= 0:
        neighbors.append(left)
    if right[0] < n:
        neighbors.append(right)

    return neighbors


def explore(pos_x, pos_y, n, nodes_visited, count):
    """
    Recurse through the matrix at each point and calculate how many
    paths exist from the current [pox_x] and [pox_y].
    """
    if pos_x == (n - 1) and pos_y == (n - 1):
        return 1
    else:
        cur_neighbors = neighbors(pos_x, pos_y, n)
        if len(cur_neighbors) == 0:
            return 0
        else:
            for neighbor in cur_neighbors:
                if neighbor not in nodes_visited:
                    nodes_visited.append((pos_x, pos_y))
                    return count + explore(
                        neighbor[0], neighbor[1], n, nodes_visited, count + 1)


def paths(n):
    """
    Calculate the total number of unique paths.
    """
    return explore(0, 0, n, [], 0)

print paths(1)
print paths(2)
print paths(3)
print paths(4)
print paths(5)
print paths(20)
