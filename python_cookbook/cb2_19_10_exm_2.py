from itertools import groupby
def paragraphs(lines, is_separator=str.isspace, joiner=''.join):
    for separator_group, lineiter in groupby(lines, key=is_separator):
        if not separator_group:
            yield joiner(lineiter)
