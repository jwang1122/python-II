"""
Issue: passing string for int without any problem.
"""
def wrapping_paper(func): 
    def wrapped(*args) -> int:  # wrapper function shoud always has same input and output data type
        print("I go a wrapped up", end=' ')
        x = func(args)
        print(f"{x} with paper.")
        return x
    return wrapped 
  
@wrapping_paper
def gift_func(giftname:int) -> int: 
    return giftname 
      
print(gift_func('gtx 5000')) 