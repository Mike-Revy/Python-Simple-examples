#   _dont_use  underscore says do not use 
# __ dunder makes inaccessibe 

class Protected: 
	__name = "Security"
	
	def __method(self):
		return self.name
	
# name mangaling
#>>> from protected import Protected
#>>> prot = Protected()
#>>> prot.__name
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Protected' object has no attribute '__name'
#>>> prot.__method
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Protected' object has no attribute '__method'
#>>> dir(prot)
#['_Protected__method', '_Protected__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
#>>> prot._Protected__name
#'Security'
#>>> prot._Protected__method
#<bound method Protected.__method of <protected.Protected object at 0x000001F3ADC67898>>
#>>>	







