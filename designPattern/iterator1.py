import time

def fib():
   a, b = 0, 1
   while True:
      yield b # rent b to caller, wait till next call
      a, b = b, a + b

if __name__ == '__main__':
    
    g = fib()

    try:
        for e in g:
            print(e)
            time.sleep(1) # use sleep to let you understand how yield works
    except KeyboardInterrupt: # Ctrl+c
        print("Calculation stopped")