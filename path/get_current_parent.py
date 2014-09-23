import os


def get_parent(start_path=None):
    if start_path is not None:
        current_dir = os.path.abspath(start_path)
    else:
        current_dir = os.path.abspath(os.path.dirname(__file__))
    base_dir = os.path.split(current_dir)[0]
    return

if __name__ == '__main__':
    main()
