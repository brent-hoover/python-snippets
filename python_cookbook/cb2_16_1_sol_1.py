def is_a_number(s):
    try: float(s)
    except ValueError: return False
    else: return True
