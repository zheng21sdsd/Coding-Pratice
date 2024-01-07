### 定义一个链表
# 链表包含数据域和下一个结点的指针域
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,data = None):
        self.head = Node(data)
    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next !=None:
            cur = cur.next
        cur.next = new_node

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(self.head.data)
        print(self.head.next.data)

    def show(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList(0)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(-1)
linked_list.show()
    # def __add__(self, other):
    #     return self.data + other.data
    # def __str__(self):
    #     return str(self.data)
    # def __repr__(self):
    #     return str(self.data)
    # def __eq__(self, other):
    #     return self.data == other.data
    # def __lt__(self, other):
    #     return self.data < other.data
    # def __gt__(self, other):
    #     return self.data > other.data
    # def __le__(self, other):
    #     return self.data <= other.data
    # def __ge__(self, other):
    #     return self.data >= other.data

# 链表的基本操作
# 1.初始化链表
# 2.遍历链表
# 3.插入结点
# 4.删除结点
# 5.修改结点
# 6.查找结点
# 7.链表的排序
# 8.链表的合并
# 9.链表的反转
# 10.链表的环检测
# 11.链表的中间结点
# 12.删除链表的倒数第N个结点
# 13.两个链表的第一个公共结点
# 14.链表的回文结点
