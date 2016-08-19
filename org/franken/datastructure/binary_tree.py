class BinaryTree:
    number = 0
    left_node = None
    right_node = None

    def __index__(self, num=0, l_node=None, r_node=None):
        self.number = num
        self.left_node = l_node
        self.right_node = r_node

    def get_number(self):
        return self.number

    def set_number(self, num):
        self.number = num

    def get_left_node(self):
        return self.left_node

    def set_left_node(self, node):
        self.left_node = node

    def get_right_node(self):
        return self.right_node

    def set_right_node(self, node):
        self.right_node = node
