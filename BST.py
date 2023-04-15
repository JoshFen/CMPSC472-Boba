
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.root = None
        self.height = 0
        self.size = 0

    def parse(self):
        root = self._parse_expression()
        if self.index < len(self.tokens):
            raise ValueError(f"Unexpected token {self.tokens[self.index]} at position {self.index}")
        return root

    def _parse_expression(self):
        left = self._parse_term()
        while self.index < len(self.tokens) and self.tokens[self.index].token_type in ["PLUS", "MINUS"]:
            op = self.tokens[self.index]
            self.index += 1
            right = self._parse_term()
            node = Node(op)
            node.left = left
            node.right = right
            left = node
        return left

    def _parse_term(self):
        left = self._parse_factor()
        while self.index < len(self.tokens) and self.tokens[self.index].token_type in ["MULTIPLY", "DIVIDE"]:
            op = self.tokens[self.index]
            self.index += 1
            right = self._parse_factor()
            node = Node(op)
            node.left = left
            node.right = right
            left = node
        return left

    def _parse_factor(self):
        if self.index >= len(self.tokens):
            raise ValueError(f"Unexpected end of expression")
        token = self.tokens[self.index]
        self.index += 1
        if token.token_type in ["INTEGER", "DECIMAL"]:
            return Node(token)
        elif token.token_type == "LPAREN":
            node = self._parse_expression()
            if self.tokens[self.index].token_type != "RPAREN":
                raise ValueError(f"Expected ) but got {self.tokens[self.index]} at position {self.index}")
            self.index += 1
            return node
        else:
            raise ValueError(f"Unexpected token {token} at position {self.index}")
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size += 1
            return
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if data < parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
        self.size += 1
        self.height = max(self.height, self.get_height(self.root))

    def delete(self, data):
        self.root = self.delete_helper(self.root, data)
        self.size -= 1
        self.height = max(self.get_height(self.root), 0)

    def delete_helper(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete_helper(node.left, data)
        elif data > node.data:
            node.right = self.delete_helper(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.get_min(node.right)
                node.data = temp.data
                node.right = self.delete_helper(node.right, temp.data)
        return node

    def get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def preorder_iterate(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_iterate(node.left)
            self.preorder_iterate(node.right)

    def inorder_iterate(self, node):
        if node is not None:
            self.inorder_iterate(node.left)
            print(node.data, end=" ")
            self.inorder_iterate(node.right)

    def postorder_iterate(self, node):
        if node is not None:
            self.postorder_iterate(node.left)
            self.postorder_iterate(node.right)
            print(node.data, end=" ")

    def value_order_iterate(self, node):
        if node is not None:
            self.value_order_iterate(node.left)
            print(node.data, end=" ")
            self.value_order_iterate(node.right)

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    def get_node_depth(self, root, target_node):
        if root is None:
            return None
        elif root == target_node:
            return 0
        else:
            left_depth = self.get_node_depth(root.left, target_node)
            if left_depth is not None:
                return left_depth + 1
            right_depth = self.get_node_depth(root.right, target_node)
            if right_depth is not None:
                return right_depth + 1
            return None
