"""
[[1,2],[3],[],[4,5,6]]

iterator::has_next() -> true
iterator::next() -> return the current element
iterator::remove() -> remove the current element

iter->has_next() -> true, iter->next() -> 1
iter->remove() -> remove 1
iter->remove() -> error
iter->has_next() -> true, iter->next() -> 2
iter->has_next() -> true, iter->next() -> 3
iter->remoe() -> remove 3
iter->has_next() -> true, iter->next() -> 4
iter->has_next() -> true, iter->next() -> 5
iter->has_next() -> true, iter->next() -> 6
iter->has_next() -> false, iter->next() -> error
print arr
[[2],[],[],[4,5,6]]
"""

class Iterator:

    outer = 0
    inner = 0

    def __init__(self, list):
        self.list = list

    def has_next(self):
        len_outer = len(self.list)
        len_inner = len(self.list[self.outer])

        if self.inner < len_inner:
            return True
        elif self.outer < len_outer:
            return True
        else:
            return False

    def next(self):
    def remove():

# def test():
#     arr = [[1,2],[3],[],[4,5,6]]
#     iter = Iterator(arr)
#     while (iter.has_next()):
#         print iter.next()

# test()
