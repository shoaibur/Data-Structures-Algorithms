class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
      
    def set_left_child(self, value):
        self.left = Node(value)
        
    def set_right_child(self, value):
        self.right = Node(value)
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left not is None
    
    def has_right_child(self):
        return self.right not is None
    
