class Product: 
    def __init__(self): 
        print("Product instance Created") 
  
    # Defining __call__ method 
    def __call__(self, a, b): 
        print(f"{a} x {b} = {a * b}") 

if __name__ == '__main__':

    # Instance created 
    add = Product() 
    
    # __call__ method will be called 
    add(10, 20) 