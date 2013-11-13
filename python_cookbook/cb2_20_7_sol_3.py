class MetaTracer(type):
    def __init__(cls, n, b, d):
        super(MetaTracer, cls).__init__(n, b, d)
        add_tracing_prints_to_all_methods(cls)
