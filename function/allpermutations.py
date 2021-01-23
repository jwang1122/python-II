"""
recursion call to print out all permutaions
"""
class Permutation:
    def __init__(self):
        self.count = 1

    def output(self, array, pos):
        if pos>=len(array)-1:
            s = "%2d:[" %self.count
            for i in range(len(array)):
                s += f"{array[i]}, "
            s = s[0:len(s)-2] + ']'
            print(s)
            self.count += 1
            return

        for i in range(pos, len(array)):
            t = array[pos]
            array[pos] = array[i]
            array[i] = t
            self.output(array, pos+1)
            t = array[pos]
            array[pos] = array[i]
            array[i] = t
        
if __name__ == '__main__':
    l = [1, 9, 3, 4]
    perm = Permutation()
    perm.output(l,0)