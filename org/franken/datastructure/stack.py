class Stack:

    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.__stack[len(self.__stack) - 1]

    def sorted_insert(self, element):
        if self.is_empty() or element > self.peek():
            self.push(element)
        else:
            temp = self.pop()
            self.sorted_insert(element)
            self.push(temp)

    def sort(self):
        if not self.is_empty():
            temp = self.pop()
            self.sort()
            self.sorted_insert(temp)


def test():
    print("stack test:")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(15)
    s.push(45)
    s.push(30)
    print(str(s.pop()) + " popped from stack")
    print("Top item is " + str(s.peek()))
    s.push(40)
    s.sort()
    print("sorted stack top item is:" + str(s.peek()))
    s.pop()
    print("sorted stack after pop top item is:" + str(s.peek()))
