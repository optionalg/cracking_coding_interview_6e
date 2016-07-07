  #!/bin/python

import re
import collections


class Element:
    """
    An 'Element' node of the DOM tree.
    @param tag: string
    @param id: string
    @param children: array of nodes which
    could be either 'Element' or 'Content' instances
    """
    def __init__(self, tag, id, children):
        self.tag = tag
        self.id = id
        self.children = children


class Content:
    """
    A 'Content' node of the DOM tree
    @param content: string
    """
    def __init__(self, content):
        self.content = content


class Dom:
    """
    A 'DOM' tree
    @param root: an instance of 'Element'
    which represents to the root of the tree
    """
    def __init__(self, root):
        self.root = root


def format(dom, whiteList):
    """
    Complete the function below.
    @param dom: An instance of the Dom class
    @param whiteList: An array of strings
    @return the output that will be sent to the STDOUT
    """
    if dom is not None:
        output = ""
        queue = []
        queue.append(dom.root)
        while queue:
            cur = queue.pop(0)
            if cur.children:
                output += "\n"
            if cur.tag:
                output += cur.tag + " "
            if cur.id:
                output += cur.id + " "
            for child in cur.children:
                if isinstance(child, Content):
                    output += child.content + " "
                elif isinstance(child, Element):
                    queue.append(child)
        return output.strip()
    else:
        return ""
