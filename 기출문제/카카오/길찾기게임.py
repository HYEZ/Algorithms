# https://programmers.co.kr/learn/courses/30/lessons/42892
# 카카오 2019 신입 공채

# 풀이) 이진트리


# 재귀 한도 늘려주기!!!
import sys
sys.setrecursionlimit(10**6)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        d, x, y = data
        if node is None:
            node = Node(data)
        else:
            if x <= node.data[1]:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def post_order_traversal(self):
        res = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                res.append(root.data[0])
        _post_order_traversal(self.root)
        return res
    
    def pre_order_traversal(self):
        res = []
        def _pre_order_traversal(root):   
            if root is None:
                pass
            else:
                res.append(root.data[0])
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
            
        _pre_order_traversal(self.root)
        return res


def solution(nodeinfo):
    tree = []
    for idx, (x, y) in enumerate(nodeinfo):
        node = (idx+1, x, y)
        tree.append(node)
    
    tree.sort(key=lambda x:(-x[2], x[1]))

    bst = BinarySearchTree()
    for data in tree:
        bst.insert(data)

    return [bst.pre_order_traversal(), bst.post_order_traversal()]

    

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	
print(solution(nodeinfo))
