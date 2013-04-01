#!/usr/bin/env python
#
# [SNIPPET_NAME: Inspect object at runtime]
# [SNIPPET_CATEGORIES: inspect]
# [SNIPPET_DESCRIPTION: inspect the objects live at runtime. In .NET world it is called Reflection]
# [SNIPPET_AUTHOR: Manish Sinha <mail@manishsinha.net>]
# [SNIPPET_DOCS: http://docs.python.org/library/inspect.html]
# [SNIPPET_LICENSE: GPL]

import inspect

# Define a sample class
class Example():
	"""A method named sample"""
	def sample(self):
		pass
	
	"""A method named foo and takes on argument"""
	def foo(self, arg):
		return "Testing";
	
	"""A Field named a"""
	a = "foo"
	
objInst= Example()
	
# Get a list of members of this instance including those from base object
memberList= inspect.getmembers(objInst)
for a in memberList:
	print(a)
	
print(inspect.ismethod(objInst.sample)) # Returns True

print(inspect.isfunction(objInst.sample)) # Returns False. Method and Function are different

print(inspect.ismodule(objInst)) # Returns False

print(inspect.isclass(Example)) # Returns true
