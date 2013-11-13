rx = re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, adict)))
