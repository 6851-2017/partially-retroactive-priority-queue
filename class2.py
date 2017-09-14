# developed by jamb and ksedlar
# C02 CODING: Partially Retroactive Priority Queue​


# very basic BBST implementation to be subclassed for what we need
class BBST:

    # class for storing Nodes of a BBST
    class Node:

        def __init__(self, parent, key, extra_data=None):
            self.parent = parent
            self.level = 0
            if parent:
                self.level = parent.level + 1
            self.key = key
            self.extra_data = extra_data
            self.left = None
            self.right = None

        def max_child(self):
            max_child = self
            if self.right:
                return self.right.max_child()
                
                
    # initialize with enough data for a first node
    def __init__(self, key, extra_data=None):
        self.root = Node(None, key, extra_data)

    # add a new node
    def insert(self, key, extra_data=None):
        parent_node = self.find(key)
        self.insert_at(parent_node, key, extra_data)

    # add a new node below a given parent
    def insert_at(self, parent, key, extra_data=None):
        new_node = Node(parent, key, extra_data)
        if parent and parent.key >= key:
            parent.left = new_node
        elif parent:
            parent.right = new_node

    def balance(self):
        # lol let's pretend this is actually a balanced tree
        # aka todo later
        return

    # point to the key if it exists in the tree
    # if not, point to the parent below which it'd be inserted
    def find(self, key_value):
        pass

    # note: don't use delete or delete-at with things that store extra_data
    def delete(self, key_value):
        key_node = self.find(key_value)
        self.delete_at(key_node)

    # note: don't use delete or delete-at with things that store extra_data
    def delete_at(self, key_node):
        if not key_node.left:
            # we can just move the right tree (which may be none) up one
            if key_node.parent and key_node.parent.key >= key:
                key_node.parent.left = key_node.right
            elif key_node.parent:
                key_node.parent.right = key_node.right
            else:
                # the key_node is the root so no parent to adjust
                self.root = key_node.right
        else:
            # we need to take the largest child from the left, delete that
            replacement_node = key_node.left.max_child()
            self.delete_at(replacement_node)
            replacement_node.parent = key_node.parent
            replacement_node.left = key_node.left
            replacement_node.right = key_node.right
            replacement_node.level = key_node.level
        

# BBST that has insertions as leaves (sorted by time)
# and internal nodes = subtree-max over x not in Qnow 
class insertions_BBST(BBST):
    pass

# BBST that stores updates sorted by time, and has extra data of
# 0/+1/-1 for permanent insert / temporary insert / delete-min
# and also stores the subtree-sum of these 0/+1/-1's
# NOTE: delete operation not supported (or needed) since it stores extra data
class bridge_BBST(BBST):
    pass
        
