from node import Node
from board import Board


class Tree:
    def __init__(self, board):
        self.__head = Node()
        self.__depth = 0
        self.__max_depth = 5
        self.__initial_board = board

    def __inverse(self, first_command, second_command):
        if first_command == 'LEFT' and second_command == 'RIGHT':
            return True
        if first_command == 'RIGHT' and second_command == 'LEFT':
            return True
        if first_command == 'UP' and second_command == 'DOWN':
            return True
        if first_command == 'DOWN' and second_command == 'UP':
            return True
        return False

    def __is_inverse(self, current_node, command):
        commands = current_node.value
        return (len(commands) > 0 and self.__inverse(commands[-1], command))

    def insert_node(self, node, value):
        new_value = list(node.value)
        new_value.append(value)
        child = Node(new_value, node.depth)
        node.add_child(child)
        return child

    def remove_node(self, from_node, value):
        from_node.remove_child(value)
