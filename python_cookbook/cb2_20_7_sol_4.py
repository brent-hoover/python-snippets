def add_tracing_prints_to_all_descendants(class_object):
    add_tracing_prints_to_all_methods(class_object)
    for s in class_object.__subclasses__():
        add_tracing_prints_to_all_descendants(s)
