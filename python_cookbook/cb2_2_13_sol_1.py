class IOManipulator(object):
    def __init__(self, function=None):
        self.function = function
    def do(self, output):
        self.function(output)
def do_endl(stream):
    stream.output.write('\n')
    stream.output.flush()
endl = IOManipulator(do_endl)
class OStream(object):
    def __init__(self, output=None):
        if output is None:
            import sys
            output = sys.stdout
        self.output = output
        self.format = '%s'
    def __lshift__(self, thing):
        ''' the special method which Python calls when you use the <<
            operator and the left-hand operand is an OStream '''
        if isinstance(thing, IOManipulator):
            thing.do(self)
        else:
            self.output.write(self.format % thing)
            self.format = '%s'
        return self
def example_main():
    cout = OStream()
    cout<< "The average of " << 1 << " and " << 3 << " is " << (1+3)/2 <<endl
# emits The average of 1 and 3 is 4
if __name__ == '__main__':
    example_main()
