from node import Node
from board import Board
import copy


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

    def BFS(self):
        to_visit_nodes = [self.__head]
        node = self.__head

        while len(to_visit_nodes) > 0:
            current_node = to_visit_nodes.pop()
            board = copy.deepcopy(self.__initial_board)

            for movement in current_node.value:
                board.move(movement)

            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            for movement in board.available_movements():
                if not self.__is_inverse(current_node, movement):
                    new_node = self.insert_node(current_node, movement)
                    to_visit_nodes.insert(0, new_node)

        return self.__initial_board, node

    def DFS(self):
        to_visit_nodes = [self.__head]
        current_node = node = self.__head

        while len(to_visit_nodes) > 0:
            current_node = to_visit_nodes.pop(0)
            board = copy.deepcopy(self.__initial_board)

            for movement in current_node.value:
                board.move(movement)

            if board.is_goal_achieved():
                node = current_node
                self.__initial_board = copy.deepcopy(board)
                break

            if current_node.depth < self.__max_depth:
                for movement in board.available_movements():
                    if not self.__is_inverse(current_node, movement):
                        new_node = self.insert_node(current_node, movement)
                        to_visit_nodes.insert(0, new_node)

        return self.__initial_board, node
