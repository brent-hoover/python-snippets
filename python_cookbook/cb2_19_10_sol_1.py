def paragraphs(lines, is_separator=str.isspace, joiner=''.join):
    paragraph = []
    for line in lines:
        if is_separator(line):
            if paragraph:
                yield joiner(paragraph)
                paragraph = []
        else:
            paragraph.append(line)
    if paragraph:
        yield joiner(paragraph)
if __name__ == '__main__':
    text = 'a first\nparagraph\n\nand a\nsecond one\n\n'
    for p in paragraphs(text.splitlines(True)): print repr(p)
