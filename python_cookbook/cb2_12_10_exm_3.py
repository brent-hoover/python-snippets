def _wrap_complete(method_name):
    def method(self, *a, **k):
        self._complete_text_node()
        getattr(XMLFilterBase, method_name)(self, *a, **k)
    # 2.4 only: method.__name__ = method_name
    setattr(text_normalize_filter, method_name, method)
