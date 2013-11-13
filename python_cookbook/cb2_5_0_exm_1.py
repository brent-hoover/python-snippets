def lexcmp(s1, s2):
     # Find leftmost nonequal pair.
     i = 0
     while i < len(s1) and i < len(s2):
         outcome = cmp(s1[i], s2[i])
         if outcome:
             return outcome
         i += 1
     # All equal, until at least one sequence was exhausted.
     return cmp(len(s1), len(s2))
