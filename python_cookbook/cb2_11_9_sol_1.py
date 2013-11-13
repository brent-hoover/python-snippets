import Tkinter, time, threading, random, Queue
class GuiPart(object):
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        # Set up the GUI
        Tkinter.Button(master, text='Done', command=endCommand).pack()
        # Add more GUI stuff here depending on your specific needs
    def processIncoming(self):
        """ Handle all messages currently in the queue, if any. """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do whatever is needed. As a
                # simple example, let's print it (in real life, you would
                # suitably update the GUI's display in a richer fashion).
                print msg
            except Queue.Empty:
                # just on general principles, although we don't expect this
                # branch to be taken in this case, ignore this exception!
                pass
class ThreadedClient(object):
    """
    Launch the main part of the GUI and the worker thread.  periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads.  We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well.  We spawn a new thread for the worker (I/O).
        """
        self.master = master
        # Create the queue
        self.queue = Queue.Queue()
        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)
        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = True
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        # Start the periodic call in the GUI to check the queue
        self.periodicCall()
    def periodicCall(self):
        """ Check every 200 ms if there is something new in the queue. """
        self.master.after(200, self.periodicCall)
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system.  You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O.  For example, it may be
        a 'select()'.  One important thing to remember is that the thread has
        to yield control pretty regularly, be it by select or otherwise.
        """
        while self.running:
            # To simulate asynchronous I/O, create a random number at random
            # intervals. Replace the following two lines with the real thing.
            time.sleep(rand.random() * 1.5)
            msg = rand.random()
            self.queue.put(msg)
    def endApplication(self):
        self.running = False
rand = random.Random()
root = Tkinter.Tk()
client = ThreadedClient(root)
root.mainloop()
