## 树的定义
递归定义：一棵树是一些节点的集合。这个集合可以是空集；若非空，则一棵树由称做根(root)的节点r以及0个或多个非空的(子)树T1, T2, ... ,Tk组成，这些子树中每一颗的根都被来自根r的一条有向的边(edge)所连接。

每一棵子树的根叫做根r的儿子(child)，而r是每一棵子树的根的父亲(parent)。

从定义中发现：一棵树是N个节点和N-1条边的集合，其中的一个节点叫做根。
没有儿子的节点称为树叶(leaf), 具有相同父亲的节点为兄弟(sibling)。

在一棵树中从根到每个节点恰好存在一条路径。

对任意节点n，n的深度(depth)为从根到n的唯一路径的长。因此，根的深度为0。
n的高(height)是从n到一片树叶的最长路径的长。一棵树的高等于它的根的高。
一个树的深度总是等于他的最深的树叶的深度；该深度总是等于这棵树的高。


## 应用
树有很多应用。流行的用法之一是包括NUIX、VAX/VMS和DOS在内的许多常用操作系统中的目录结构。

> 在UNIX文件系统中的目录就是含有他的所有儿子的一个文件。

## 二叉树(binary tree)
二叉树是一棵树，其中给每个节点都不能有多于两个的儿子。

树节点的声明在结构上类似于双链表的声明，一个节点就是由Key(关键字)信息加上两个指向其他节点的指针组成。

> 具有N个节点的每一棵二叉树都将需要N+1个NULL指针。

**二叉树节点声明**
``` C
typedef struct TreeNode *PtrToNode;
typedef struct PtrToNode Tree;

struct TreeNode
{
    ElementType Element;
    Tree        Left;
    Tree        Right;
}

```

### 二叉查找树(binary search tree)
又叫二叉搜索树，二叉排序树。
对于树中的每个节点X，它的左子树中所有关键字值小于X的值，而右子树中所有关键字值大于X的值。

因为二叉查找树的平均深度是O(logN)，所以一般不必担心栈空间被用尽。

### AVL树
AVL(Adelson-Velskii和Landis)树是带有平衡条件的二叉查找树。坐着个平衡条件必须容易保持，而且它须保证树的深度是O(logN)。
一棵AVL树是其每个节点的左子树和右子树的高度最多差1的二叉查找树。

## 树的遍历
按顺序打印二叉查找树(中序遍历，运行时间O(N))
``` C
typedef struct TreeNode *SearchTree;

void
PrintTree(SearchTree T)
{
    if(T != NULL)
    {
        PrintTree(T->Left);
        PrintElement(T->Element);
        PrintTree(T->Right);
    }
}
```

使用后序遍历计算树的高度
``` C
int
Height(Tree T)
{
    if(T == NULL)
        return -1;
    else
        return 1 + Max(Height(T->Left, Height(T->Right)));
}
```


## 参考
《数据结构与算法分析---C语言描述》 by [美] Mark Allen Weiss