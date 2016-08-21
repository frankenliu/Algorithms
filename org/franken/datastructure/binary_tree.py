class Node:

    def __init__(self, num=0):
        self.__number = num
        self.__left_node = None
        self.__right_node = None

    def get_number(self):
        return self.__number

    def set_number(self, num):
        self.__number = num

    def get_left_node(self):
        return self.__left_node

    def set_left_node(self, node):
        self.__left_node = node

    def get_right_node(self):
        return self.__right_node

    def set_right_node(self, node):
        self.__right_node = node
