import sys


class myScraper():
    def __init__(self, fileName=""):
        self.fileName = fileName

    def test(self):
        print(f"Hello {self.fileName}!")


def main(fileName):
    obj = myScraper(fileName)
    obj.test()

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else "")