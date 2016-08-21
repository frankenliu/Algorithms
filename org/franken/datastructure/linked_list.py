class Node:

    def __init__(self, num=0, node=None):
        self.__number = num
        self.__next_node = node

    def get_number(self):
        return self.__number

    def set_number(self, num):
        self.__number = num

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, node):
        self.__next_node = node

