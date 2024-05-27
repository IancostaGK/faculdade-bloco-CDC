class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

#Q1 Escreva um programa que implemente uma árvore binária de busca balanceada, do tipo AVL.
class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, root):
        if not root:
            return 0
        return root.height

    def _getBalance(self, root):
        if not root:
            return 0
        return self._height(root.left) - self._height(root.right)

    def _leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left),
                            self._height(z.right))
        y.height = 1 + max(self._height(y.left),
                            self._height(y.right))

        return y

    def _rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._height(y.left),
                            self._height(y.right))
        x.height = 1 + max(self._height(x.left),
                            self._height(x.right))

        return x

    #Q2 Escreva uma função/método para fazer a inserção de elementos na árvore implementada na questão 1.
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._height(root.left),
                                self._height(root.right))

        balance = self._getBalance(root)

        if balance > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balance < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def inorderTraversal(self):
        self._inorderTraversal(self.root)
        print()

    def _inorderTraversal(self, root):
        if root:
            self._inorderTraversal(root.left)
            print(root.key, end=' ')
            self._inorderTraversal(root.right)

    # Q3 Escreva uma função/método para executar buscas na árvore implementada na questão 1.
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root
        if root.key < key:
            return self._search(root.right, key)
        return self._search(root.left, key)

    # Q4 Escreva uma função/método para fazer a remoção de nodos os elementos na árvore implementada na questão 1.
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)

        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._minValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self._height(root.left),
                                self._height(root.right))

        balance = self._getBalance(root)

        if balance > 1:
            if self._getBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balance < -1:
            if self._getBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

if __name__ == "__main__":
    tree = AVLTree()
    keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90]

    for key in keys:
        tree.insert(key)

    print("Árvore AVL em ordem:")
    tree.inorderTraversal()

    search_keys = [40, 100, 25, 55]
    for key in search_keys:
        result = tree.search(key)
        if result:
            print(f"Elemento {key} encontrado na árvore AVL.")
        else:
            print(f"Elemento {key} não encontrado na árvore AVL.")

    delete_keys = [30, 70, 50]
    for key in delete_keys:
        tree.delete(key)
        print(f"Elemento {key} removido. Árvore após remoção:")
        tree.inorderTraversal()
