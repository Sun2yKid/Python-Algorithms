class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        if self.head:
            node = self.head
            while node:
                yield node
                node = node.next
        else:
            return []

    def __repr__(self):
        """
        only used for link list that isn't big
        """
        linked_list = []
        for _node in self:
            linked_list.append(_node.data)
        return '->'.join(linked_list)

    @property
    def tail(self):
        for _node in self:
            if _node.next is None:
                return _node
        return self.head

    def append(self, data):
        if self.head:
            self.tail.next = ListNode(data)
        else:
            self.head = ListNode(data)

    def print_list(self):
        for _node in self:
            print(_node.data, end='->')
        print('None')


ll = LinkedList()
print(ll, type(ll), ll.head, ll.tail)
ll.append('a')
print(ll)
ll.append('b')
ll.append('c')
print(ll)
print('head:', ll.head.data)
print('tail:', ll.tail.data)
ll.print_list()
