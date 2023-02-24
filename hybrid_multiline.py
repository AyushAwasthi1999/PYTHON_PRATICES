class a:
    def displaya(self):
        print("class a")

class b(a):
    def displayb(self):
        print("class b")

class c(a):
    def displayc(self):
        print("class c")

class d(b,c)
