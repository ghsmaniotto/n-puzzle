class Node:
    def __init__(self, value=list(), parent_depth=-1):
        self.value = value
        self.depth = parent_depth + 1
        self.__childs = []

    def add_child(self, node):
        if self.__existed_child(node.value):
            return
        else:
            self.__childs.append(node)
            return node

    def remove_child(self, value):
        self.__childs.remove(
            list(filter(lambda x: x.value == value, self.__childs))[0]
        )

    def get_childs(self):
        return self.__childs

    def __existed_child(self, value):
        len(list(filter(lambda x: x.value == value, self.__childs))) > 0
