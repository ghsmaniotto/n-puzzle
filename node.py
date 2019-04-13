class Node:
    def __init__(self, value=list(), parent_depth=-1):
        self.value = value
        self.depth = parent_depth + 1
        self.__childs = []

    def add_child(self, node):
        """ Inserts a child in the node.

        Keyword arguments:
        node -- node to insert a new child
        """
        if self.__existed_child(node.value):
            return
        else:
            self.__childs.append(node)
            return node

    def remove_child(self, value):
        """ Removes a child in the node.

        Keyword arguments:
        value -- value to be removed
        """
        self.__childs.remove(
            list(filter(lambda x: x.value == value, self.__childs))[0]
        )

    def __existed_child(self, value):
        """ Check if the value already exists in node child.

        Keyword arguments:
        value -- value to be checked
        """
        len(list(filter(lambda x: x.value == value, self.__childs))) > 0
