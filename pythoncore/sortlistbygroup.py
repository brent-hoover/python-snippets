# [SNIPPET_NAME: Sort list by group]
# [SNIPPET_CATEGORIES: Python Core]
# [SNIPPET_DESCRIPTION: This function takes a list of string and sorts them based on their similarity. The percent at which they match can be defined in the second parameter (default 75%)]
# [SNIPPET_AUTHOR: John Turek <jt@dweeb.net>]
# [SNIPPET_LICENSE: GPL]


def sortByGroup(lst, percent=75):
    groups = []
    for item in lst:
        match = False

        for g in xrange(len(groups)):
            group = groups[g]
            parent = group[0]
            points = 0.0

            try:
                for x in xrange(len(parent)):
                    if parent[x] == item[x]:
                        points += 1

                if (points / len(parent)) * 100 >= percent:
                    group.append(item)
                    group.sort()
                    match = True
            except:
                pass

        if not match:
            groups.append([item])

    return groups


# Example:
random = [
    'bob1',
    'frank2',
    'bob3',
    'joe2',
    'frank1',
    'bob2',
    'joe1',
    'joe3'
]
groups = sortByGroup(random)
for g in groups:
    for i in g:
        print i
    print '-' * 30
