def nextSquare(start, step): 
	i = start;

	while True: 
		yield round(i+step,2)				 
		i += step # Next execution resumes from this point	 

def frange(start, stop, step):
    for num in nextSquare(start, step): 
	    if num > stop: 
		    break	
	    print(num) 

frange(1,5, 0.2)