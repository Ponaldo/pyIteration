class StringIter:
    b = 0

    def __init__(self, stringex, delim):
        self.stringex = stringex
        self.delim = delim
        self.x = self.stringex.split(self.delim)

    def wordcount(self):
        return len(self.x)

    def __iter__(self):
        self.a = self.x[self.b]
        return self

    def __next__(self):
        c = self.x[self.b]
        self.b += 1
        return c


def main():
    s = input("Hello input string: ")
    d = input("delimiter: ")
    mystring = StringIter(s, d)
    print("There are " + str(mystring.wordcount()) + " words in the sentence")
    myiter = iter(mystring)
    for x in range(mystring.wordcount()):
        print(next(myiter))


main()
