"""
Issue: passing string for int without any problem.
"""
def wrapping_paper(func): 
    def wrapped(gift:int): 
        return 'I got a wrapped up {} for you'.format(str(func(gift))) 
    return wrapped 
  
@wrapping_paper
def gift_func(giftname:int) -> int: 
    return giftname 
      
print(gift_func('gtx 5000')) 