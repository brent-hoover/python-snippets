data = [float(line) for line in open(some_file)
                    if not throws(ValueError, float, line)]
