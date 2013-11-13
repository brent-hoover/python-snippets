text = """ Indeed, it has been said that democracy is the worst form of
    government, except for all those others that have been tried
    from time to time. """
import string
for a, b in [("democracy", "SQL"), ("government", "database")]:
    text = string.replace(text, a, b)
print text
