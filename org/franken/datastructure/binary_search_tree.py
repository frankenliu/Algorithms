from org.franken.datastructure.binary_tree import Node


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, key):
        self.__root = self.insert_rec(self.__root, key)

    def insert_rec(self, root, key):
        r = root
        if r is None:
            r = Node(key)
        else:
            if r.get_number() > key:
                r.set_left_node(self.insert_rec(r.get_left_node(), key))
            else:
                r.set_right_node(self.insert_rec(r.get_right_node(), key))
        return r

    def get_min_value_node(self, root):
        current = root
        while current.get_left_node() is not None:
            current = current.get_left_node()
        return current

    def delete(self, key):
        self.__root = self.delete_rec(self.__root, key)

    def delete_rec(self, root, key):
        if root is None:
            return root
        r = root
        if r.get_number() > key:
            r.set_left_node(self.delete_rec(r.get_left_node(), key))
        elif r.get_number() < key:
            r.set_right_node(self.delete_rec(r.get_right_node(), key))
        else:
            if r.get_left_node() is None:
                return r.get_right_node()
            elif r.get_right_node is None:
                return r.get_left_node()
            temp = self.get_min_value_node(r.get_right_node())
            r.set_number(temp.get_number())
            r.set_right_node(self.delete_rec(r.get_right_node(), temp.get_number()))
        return r

    def in_order(self):
        self.in_order_rec(self.__root)

    def in_order_rec(self, root):
        if root:
            self.in_order_rec(root.get_left_node())
            print(root.get_number())
            self.in_order_rec(root.get_right_node())


def test():
    tree = BinarySearchTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)
    print("binary search tree:")
    tree.in_order()
    print("binary search tree delete:")
    tree.delete(70)
    tree.in_order()
