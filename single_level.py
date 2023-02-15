#Single Level Inheritance

class parent :
    def display_parent(self):
        print("This is Parents Class")

class child(parent):
    def display_child(self):
        print("This is child Class")

obj = child()
obj.display_parent()
obj.display_child()
