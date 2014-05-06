def check_basic_auth(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            # NOTE: We are only support basic authentication for now.
            #
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).split(':')
                user = authenticate(username=uname, password=passwd)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.user = user
    return request


def check_session_auth(request):
    if request.user.is_authenticated():
        return True


def check_auth(request):
    if request.user.is_authenticated():
        return True
    else:
        # They are not logged in. See if they provided login credentials
        request = check_basic_auth(request)
        if request.user.is_authenticated():
            return True
        else:
            return False

def view_or_basicauth(view, request, test_func, realm = "", *args, **kwargs):
    """
    This is a helper function used by both 'logged_in_or_basicauth' and
    'has_perm_or_basicauth' that does the nitty of determining if they
    are already logged in or if they have provided proper http-authorization
    and returning the view if all goes well, otherwise responding with a 401.
    """
    if check_auth(request):
        return view(request, *args, **kwargs)

    # Either they did not provide an authorization header or
    # something in the authorization attempt failed. Send a 401
    # back to them to ask them to authenticate.
    #
    response = HttpResponse('Auth Required')
    response.status_code = 401
    response['WWW-Authenticate'] = 'Basic realm="%s"' % realm
    return response

#############################################################################


def logged_in_or_basicauth(view_func):
    """
    The existing loggged_in_or_basic does not properly pass along arguments
    so I wrote this one temporarily to see if I can replace it
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        checked_basic_auth = None
        if request.user.is_anonymous():
            request = check_basic_auth(request)
            checked_basic_auth = True
        if check_session_auth(request):
            return view_func(request, *args, **kwargs)
        else:
            response = HttpResponse('Auth Required: user was %s and check_basic: %s' % (request.user, checked_basic_auth))
            response.status_code = 401
            return response
    return wrapper
