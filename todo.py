class Todo:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    # referenced by programmers
    # repr is representation of your code and tells you how to initialize your code.      
    def __repr__(self):
        # return f"Todo('{self.name}')"
        return f"{__class__.__name__}('{self.name}')"

    # referenced by users
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.items)

    def __gt__(self,other):
        return len(self.items) > len(other.items)

    def __lt__(self, other):
        return len(self.items) < len(other.items)   



