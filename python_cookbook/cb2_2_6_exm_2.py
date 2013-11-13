import re
def words_by_re(thefilepath, repattern=r"[\w'-]+"):
    wre = re.compile(repattern)
    def line_to_words(line):
        for mo in wre.finditer(line):
            return mo.group(0)
    return words_of_file(thefilepath, line_to_words)
