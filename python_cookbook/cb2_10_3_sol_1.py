def popauth(popHost, user, passwd):
    """ Log in and log out, only to verify user identity.
        Raise exception in case of failure.
    """
    import poplib
    try:
        pop = poplib.POP3(popHost)
    except:
        raise RuntimeError("Could not establish connection "
                           "to %r for password check" % popHost)
    try:
        # Log in and perform a small sanity check
        pop.user(user)
        pop.pass_(passwd)
        length, size = pop.stat()
        assert type(length) == type(size) == int
        pop.quit()
    except:
        raise RuntimeError("Could not verify identity. \n"
              "User name %r or password incorrect." % user)
        pop.quit()
