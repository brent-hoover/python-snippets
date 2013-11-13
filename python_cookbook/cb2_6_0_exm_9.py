class OneMore(Behave):
    def repeat(self, N): Behave.repeat(self, N+1)
zealant = OneMore("Worker Bee")
zealant.repeat(3)
