class MyClass:    
	variable = "blah"    
	def function(self):        
		print("This is a message inside the class.")

if __name__ == '__main__':
	myobject = MyClass()

	print(myobject.variable)
	myobject.function()
