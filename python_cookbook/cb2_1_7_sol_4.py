import re
revwords = re.split(r'(\s+)', astring)    # separators too, since '(...)'
revwords.reverse()                        # reverse the list in place
revwords = ''.join(revwords)              # list of strings -> string
