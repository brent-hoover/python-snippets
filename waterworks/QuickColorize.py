#!/usr/bin/env python

"""QuickColorize: provides a quick way to randomly colorize text.
By calling colorize() on text, it will randomly assign a color for
that text (which will be reused on subsequent calls to colorize().
Also includes a command-line mode."""

# TODO use bg colors
import ansi, itertools
all_colors = [name for name in dir(ansi) if name[0].isupper()]
fg_colors = sorted([name for name in all_colors if not name.endswith('BG')])
bg_colors = sorted([name for name in all_colors if name.endswith('BG')])

for name in 'BLACK BOLD REVERSE RESET'.split():
    fg_colors.remove(name)

# put black first
bg_colors.remove('BLACKBG')
bg_colors.insert(0, 'BLACKBG')

color_pairs = []
for bg_color in bg_colors:
    for fg_color in fg_colors:
        if bg_color.startswith(fg_color):
            continue
        if bg_color == 'BLACKBG' and fg_color == 'WHITE':
            continue

        color_pairs.append((fg_color, bg_color))

color_cycler = itertools.cycle(color_pairs)
colors_defined = {}
def colorize(text):
    """Returns a colorized version of text.  The same text values will
    be consistently colorized."""
    color = colors_defined.get(text)
    if not color:
        names = color_cycler.next()
        colors = [getattr(ansi, name) for name in names]
        colors_defined[text] = color
    return ''.join(colors) + text + ansi.RESET

if __name__ == "__main__":
    # a quick command-line program for colorizing stdin or a list of files

    # Example:
    # % quickcolorize term1 term2 term3 < somefilename
    # Use -- to separate terms to highlight from filenames:
    # % quickcolorize term1 term2 term3 -- file1 file2 file3
    import sys

    filenames = []
    stdin_mode = True

    mapping = {}
    for arg in sys.argv[1:]:
        if arg == '--':
            stdin_mode = False
            continue
        if stdin_mode:
            mapping[arg] = colorize(arg)
        else:
            filenames.append(arg)

    def file_iter():
        if stdin_mode:
            yield sys.stdin
        else:
            for filename in filenames:
                f = file(filename)
                yield f
                del f

    for input_file in file_iter():
        for line in input_file:
            for old, new in mapping.items():
                line = line.replace(old, new)
            try:
                sys.stdout.write(line)
            except IOError:
                raise SystemExit
