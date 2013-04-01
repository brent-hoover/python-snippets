"""Convert a Python table into a LaTeX/TeX table."""
__all__ = ['texify', 'make_tex_bitmap']

def texify(table, compact=1, has_header=False, hlines=True, vlines=True):
    """compact is a value from 0 to 2 which controls how much whitespace
    we output.  It does not change the display of the table."""
    s = []
    xdim = len(table[0])

    if compact == 0:
        compact1 = compact2 = '\n'
    elif compact == 1:
        compact1 = '\n'
        compact2 = ''
    else:
        compact1 = ' '
        compact2 = ''

    if hlines:
        hline_text = r'\hline'
    else:
        hline_text = ''
    if vlines:
        separator = '|'
    else:
        separator = ''

    s.append(r"\begin{tabular}{" + 'c'.join(([separator] * (xdim + 1))) + "}\n")
    if hlines:
        s.append(hline_text + "\n")
    for count, row in enumerate(table):
        s.append(' & '.join([str(x) for x in row]) + compact1)
        if has_header and count == 0:
            s.append(r"\\ %s%s%s%s" % (hline_text, hline_text, '\n', compact2))
        else:
            s.append(r"\\ " + hline_text + "\n" + compact2)
    s.append(r"\end{tabular}")

    return ''.join(s)

def greyify_cell(cell, white_is_1=False, value_formatter=None):
    if isinstance(cell, (float, int)) and 0 <= cell <= 1:
        if not white_is_1:
            cell = 1 - cell
        result = r'\cellcolor[gray]{%0.3f}' % cell
        if value_formatter:
            result += ' ' + str(value_formatter(cell))
        return result
    else:
        return cell

# XXX TODO more docs
def make_tex_bitmap(table, has_header=False, white_is_1=True, 
                    value_formatter=None):
    """All floats will be converted to their grey values.  You will need
    to include the LaTeX package colortbl:

        \usepackage{colortbl}

    has_header is passed to texify."""
    rows = [[greyify_cell(cell, white_is_1=white_is_1, 
                          value_formatter=value_formatter) 
                for cell in row] 
            for row in table]
    return texify(rows, has_header=has_header)

if __name__ == "__main__":
    print texify([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print
    print make_tex_bitmap([[0.1, 0.2, 0.3]])
