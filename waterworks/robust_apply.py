"""Simple front-end to louie.robustapply.robust_apply.  This has been
abstracted to make the implementation more portable and not tied to
specific dispatcher packages."""

import louie.robustapply 

def robust_apply(func, *args, **kwargs):
    """Almost identical to louie.robustapply.robust_apply except that it
    forces func and signature to be identical."""
    return louie.robustapply.robust_apply(func, func, *args, **kwargs)

if __name__ == "__main__":
    def test(a, b, c):
        print 'test', (a, b, c)

    robust_apply(test, a=1, b=2, c=3, d=5)
    robust_apply(test, 1, b=2, c=3, d=5)
