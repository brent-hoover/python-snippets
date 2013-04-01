"""Tools for creating tables and figures in papers."""
from sets import Set
import sys

def dict_to_table(d, headers=True, x_header='', reverse=False):
    """Convert dict with (x, y) as keys to a 2D table."""
    all_x = Set()
    all_y = Set()
    for x, y in d.keys():
        all_x.add(x)
        all_y.add(y)
    all_x = list(all_x)
    all_y = list(all_y)
    all_x.sort()
    all_y.sort()
    if reverse:
        if 'x' in reverse:
            all_x.reverse()
        if 'y' in reverse:
            all_y.reverse()

    if headers:
        table = [[x_header] + all_y]
    else:
        table = []
    for i, x in enumerate(all_x):
        row = [None] * len(all_y)
        for j, y in enumerate(all_y):
            row[j] = d.get((x, y))
        if headers:
            row.insert(0, x)
        table.append(row)
    return table

supported_formats = ('csv', 'tsv', 'tex', 'texbitmap', 'asciiart')
def format_table(table, format='csv', outputstream=sys.stdout, **extra_options):
    """table can be a table from dict_to_table() or a dictionary.
    The dictionary can have either a single value as a key (for a
    one-dimensional table) or 2-tuples (for two-dimensional tables).
    format is currently one of csv, tsv, tex, texbitmap, or asciiart.
    Values for texbitmap should be floats between 0 and 1 and the output
    will be the TeX code for a large-pixeled bitmap."""
    if isinstance(table, dict):
        table = dict_to_table(table)

    if format in ('csv', 'tsv'):
        import csv
        dialect = {'csv' : csv.excel, 'tsv' : csv.excel_tab}[format]
        writer = csv.writer(outputstream, dialect=dialect)
        for row in table:
            writer.writerow(row)
    elif format == 'tex':
        import TeXTable
        print >>outputstream, TeXTable.texify(table, has_header=True)
    elif format == 'texbitmap':
        import TeXTable
        extra_options.setdefault('has_header', True)
        print >>outputstream, TeXTable.make_tex_bitmap(table, **extra_options)
    elif format == 'asciiart':
        from texttable import Texttable
        texttable = Texttable(**extra_options)
        texttable.add_rows(table)
        print >>outputstream, texttable.draw()
    else:
        raise ValueError("Unsupported format: %r (supported formats: %s)" % \
            (format, ' '.join(supported_formats)))

if __name__ == "__main__":
    print dict_to_table({('add-0', '01') : 7,
                         ('add-0', '22') : 8,
                         ('add-0', '24') : 9,
                         ('add-1', '01') : 10,
                         ('add-1', '22') : 11,
                         ('add-1', '24') : 12,})
    format_table(dict_to_table({('add-0', '01') : 7,
                         ('add-0', '22') : 8,
                         ('add-0', '24') : 9,
                         ('add-1', '01') : 10,
                         ('add-1', '22') : 11,
                         ('add-1', '24') : 12,}), format='tsv')
