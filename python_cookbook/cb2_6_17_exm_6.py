class SeqNull(Null):
    def __len__(self): return 0
    def __iter__(self): return iter(())
    def __getitem__(self, i): return self
    def __delitem__(self, i): return self
    def __setitem__(self, i, v): return self
