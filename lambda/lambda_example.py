"""
The lambda operator built in to the Python language provides a method to create 
anonymous functions. This makes it easier to pass simple functions as parameters 
or assign them to variable names. The lambda operator uses the following syntax 
to define the function: lambda : The term args refers to a list of arguments 
that get passed to the function. The term expression can be any legal Python 
expression. The following code shows an example of using the lambda operator to 
assign an anonymous function to a variable:');
"""
>>>bigger = lambda a, b : a > b
>>>print bigger(1,2)
False
>>>print bigger(2,1)
True
