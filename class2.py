# developed by jamb and ksedlar
# C02 CODING: Partially Retroactive Priority Queue​


# very basic BBST implementation to be subclassed for what we need
class BBST:

    # class for storing Nodes of a BBST
    class Node:
        
        def __init__(self, parent, key, extra_data)
            self.parent = parent
            self.key = key
            self.extra_data = extra_data
            self.left = None
            self.right = None
                
    # initialize with enough data for a first node
    def __init__(self, key, extra_data):
        self.root = Node(None, key, extra_data)

    # add a new node
    def insert(self, parent, key, extra_data):
        new_node = Node(parent, key, extra_data)
        if parent and parent.key >= key:
            parent.left = new_node
        elif parent:
            parent.right = new_node

    def balance(self):
        # lol let's pretend this is actually a balanced tree
        # aka todo later
        return

# BBST for storing the elements of Qnow
class Qnow_BBST:
    pass

# BBST that has insertions as leaves (sorted by time)
# and internal nodes = subtree-max over x not in Qnow 
class insertions_BBST:
    pass

# BBST that stores updates sorted by time, and has extra data of
# 0/+1/-1 for permanent insert / temporary insert / delete-min
# and also stores the subtree-sum of these 0/+1/-1's
class bridge_BBST:
    pass
        
