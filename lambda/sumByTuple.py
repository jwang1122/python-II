# Python3 code to demonstrate working of  
# Tuple to Dictionary Summation conversion 
# Using defaultdict() + loop 
from collections import defaultdict 
  
# initializing list 
test_list = [(7, 8), (5, 6), (7, 2), (6, 8), (5, 10)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# Tuple to Dictionary Summation conversion 
# Using defaultdict() + loop 
res = defaultdict(int) 
for sub in test_list: 
    res[sub[0]] += sub[1] 
  
# printing result  
print("The summation tuple dictionary : " + str(dict(res)))
key=5
print(f"Sum on key={key} is {res[key]}")