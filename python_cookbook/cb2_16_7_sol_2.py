import tokenize, cStringIO
# in 2.3, also do 'from sets import Set as set'
mergers = {':' : set('=+'), }
def tokens_of(x):
    it = peek_ahead(toktuple[1] for toktuple in
            tokenize.generate_tokens(cStringIO.StringIO(x).readline)
         )
    # in 2.3, you need to add brackets [ ] around the arg to peek_ahead
    for tok in it:
        if it.preview in mergers.get(tok, ()):
            # merge with next token, as required
            yield tok+it.next()
        elif tok[:1].isdigit() and '.' in tok:
            # split if digits on BOTH sides of the '.'
            before, after = tok.split('.', 1)
            if after:
                # both sides -> yield as 3 separate tokens
                yield before
                yield '.'
                yield after
            else:
                # nope -> yield as one token
                yield tok
        else:
            # not a merge or split case, just yield the token
            yield tok
