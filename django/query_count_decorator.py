def check_query_count(num_queries):
    def decorator(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            initial_queries = len(connection.queries)
            ret = func(self, *args, **kwargs)
            final_queries = len(connection.queries)
            if settings.DEBUG:
                self.assertEqual(final_queries - initial_queries, num_queries)
            return ret
        return inner
    return decorator
