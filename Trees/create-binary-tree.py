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
        
