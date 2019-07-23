class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.value < value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

    def get_max(self):
        if self.value is None:
            return None
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        if self.value is None:
            return None
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
        return cb(self.value)
