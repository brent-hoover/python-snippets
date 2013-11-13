class NiceClass(object):
    def __init__(self, name):
        self.nice_new_name = name
    bad_old_name = OldAlias('nice_new_name', 'bad_old_name')
