from enum import IntFlag
"""
IntFlag allow bitwise operations (&, |, ^, ~)
"""
class Perm(IntFlag):
    R = 4
    W = 2
    Z = 1
    RWX = 7

if __name__ == '__main__':
    print((Perm.R | Perm.W).value)
    print((Perm.R + Perm.W))
    rw = Perm.R | Perm.W
    print(Perm.R in rw)
    print(~Perm.RWX)
    x = ~Perm.RWX.value
    print(x)
    x = Perm.R & Perm.W
    print(x.value)