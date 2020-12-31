class SubSet:
    def getSubsets(self, masterSet):
        return self.subsetsRecur([], sorted(masterSet))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

if __name__ == '__main__':
    print(SubSet().getSubsets([4,5,6]))