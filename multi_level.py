#multi- Level Inheritance

class parent :
    def display_parent(self):
        print("This is Parents Class")
        
class parent2:
    def display_parent2(self):
        print("This is Parents2 Class")

class child(parent,parent2):
    def display_child(self):
        print("This is child Class")

obj = child()
# obj.display_parent()
obj.display_parent2()
obj.display_child()
