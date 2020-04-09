class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display_tree(tree):    # 中序遍历，递归方式
    if tree:
        display_tree(tree.left)
        print(tree.data)
        display_tree(tree.right)


def height_of_tree(tree):   # 树叶的高度是0
    if tree is None:
        return -1
    else:
        return 1 + max([height_of_tree(tree.left), height_of_tree(tree.right)])


def is_full_binary_tree(tree):
    if tree is None:
        return True
    return is_full_binary_tree(tree.left) ^ is_full_binary_tree(tree.right)


def main():  # Main func for testing.
    """
                    1
                  /   \
                2      3
               / \    /
              4   5  7
                 /   \
                6     8
                       \
                        9
    """
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.right = Node(8)
    tree.right.left.right.right = Node(9)

    display_tree(tree)
    print('depth of tree:', height_of_tree(tree))
    print('is_full_binary_tree:', is_full_binary_tree(tree))


if __name__ == '__main__':
    main()
