from cStringIO import StringIO
class RewindableFile(object):
    """ Wrap a file handle to allow seeks back to the beginning. """
    def __init__(self, input_file):
        """ Wraps input_file into a file-like object with rewind. """
        self.file = input_file
        self.buffer_file = StringIO()
        self.at_start = True
        try:
            self.start = input_file.tell()
        except (IOError, AttributeError):
            self.start = 0
        self._use_buffer = True
    def seek(self, offset, whence=0):
        """ Seek to a given byte position.
        Must be: whence == 0 and offset == self.start
        """
        if whence != 0:
            raise ValueError("whence=%r; expecting 0" % (whence,))
        if offset != self.start:
            raise ValueError("offset=%r; expecting %s" % (offset, self.start))
        self.rewind()
    def rewind(self):
        """ Simplified way to seek back to the beginning. """
        self.buffer_file.seek(0)
        self.at_start = True
    def tell(self):
        """ Return the current position of the file (must be at start).  """
        if not self.at_start:
            raise TypeError("RewindableFile can't tell except at start of file")
        return self.start
    def _read(self, size):
        if size < 0:             # read all the way to the end of the file
            y = self.file.read()
            if self._use_buffer:
                self.buffer_file.write(y)
            return self.buffer_file.read() + y
        elif size == 0:          # no need to actually read the empty string
            return ""
        x = self.buffer_file.read(size)
        if len(x) < size:
            y = self.file.read(size - len(x))
            if self._use_buffer:
                self.buffer_file.write(y)
            return x + y
        return x
    def read(self, size=-1):
        """ Read up to 'size' bytes from the file.
        Default is -1, which means to read to end of file.
        """
        x = self._read(size)
        if self.at_start and x:
            self.at_start = False
        self._check_no_buffer()
        return x
    def readline(self):
        """ Read a line from the file. """
        # Can we get it out of the buffer_file?
        s = self.buffer_file.readline()
        if s[-1:] == "\n":
            return s
        # No, so read a line from the input file
        t = self.file.readline()
        if self._use_buffer:
            self.buffer_file.write(t)
        self._check_no_buffer()
        return s + t
    def readlines(self):
        """read all remaining lines from the file"""
        return self.read().splitlines(True)
    def _check_no_buffer(self):
        # If 'nobuffer' has been called and we're finished with the buffer file,
        # get rid of the buffer, redirect everything to the original input file.
        if not self._use_buffer and \
               self.buffer_file.tell() == len(self.buffer_file.getvalue()):
            # for top performance, we rebind all relevant methods in self
            for n in 'seek tell read readline readlines'.split():
                setattr(self, n, getattr(self.file, n, None))
            del self.buffer_file
    def nobuffer(self):
        """tell RewindableFile to stop using the buffer once it's exhausted"""
        self._use_buffer = False
