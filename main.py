class MyNums:
    def __init__(self, testnum):
        self.testnum = testnum

    def __iter__(self):
        self.a = self.testnum + 20
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

y = int(input("Input the beginning number "))
myclass = MyNums(y)
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

