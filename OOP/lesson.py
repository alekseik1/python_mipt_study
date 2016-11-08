class test:
    def __init__(self):
        self.a = 2
    def doSome(self):
        return self.a
b = test()
b.a = 2
print(b.doSome())
