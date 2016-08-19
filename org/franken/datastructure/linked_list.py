class LinkedList:
    number = 0
    next_node = None

    def __init__(self, num=0, node=None):
        self.number = num
        self.next_node = node

    def get_number(self):
        return self.number

    def get_next_node(self):
        return self.next_node