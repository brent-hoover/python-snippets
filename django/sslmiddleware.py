
from django.core.urlresolvers import resolve
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.contrib.sites.models import Site
import re

CURRENT_DOMAIN = Site.objects.get(id=settings.SITE_ID).domain
HREF_PATTERN = re.compile(r"""href\s*=\s*["'']([^"'']+)["'']""", re.IGNORECASE)

def secure(func):
    """ Decorator for secure views. """
    def _secure(*args, **kwargs):
        return func(*args, **kwargs)
    _secure.is_secure = True
    _secure.__name__ = func.__name__
    return _secure

class SSLMiddleware(object):
    """ Redirects requests and rewrites URLs to correct HTTP/HTTPS protocol.

    Based on use of @secure decorator above to specify HTTPS views.

    The process_request method also intercepts insecure requests for secure
    methods and vice-versa and returns a permanent HTTP redirect to the
    correct URL.

    The process_response method prepends the correct protocol and domain as
    required to href attributes within HTML responses:
    
    - If request is secure, all absolute URLs which resolve to non-@secure
      views (or begin with MEDIA_URL) will be prepended with
      http://<CURRENT_DOMAIN>
    - If request is not secure, all URLs which resolve to @secure views will
      be prepended with https://<CURRENT_DOMAIN>
    - Relative URLs and fully-qualified URLs (anything that doesn''t begin with
      a forward slash) is left untouched.

    """

    def _add_protocol(self, protocol, url):
        return ''%s://%s%s'' % (protocol, CURRENT_DOMAIN, url)

    def _resolves_to_secure_view(self, url):
        try:
            view_func, args, kwargs = resolve(url)
        except:
            return None
        else:
            return getattr(view_func, ''is_secure'', False)

    def _correct_protocol(self, request, url):
        if request.is_secure():
            if url.startswith(settings.MEDIA_URL):
                if url.startswith(''/''):
                    url = self._add_protocol(''http'', url)
            elif url.startswith(''/''):
                if not self._resolves_to_secure_view(url):
                    url = self._add_protocol(''http'', url)
        else:
            if url.startswith(''/''):
                if self._resolves_to_secure_view(url):
                    url = self._add_protocol(''https'', url)
        return url
                    
    def process_request(self, request):
        """ Redirect request if protocol incorrect """
        url = self._correct_protocol(request, request.path)
        if url != request.path:
            if request.method == ''GET'':
                return HttpResponsePermanentRedirect(url)
            elif settings.DEBUG:
                raise RuntimeError, ''Cannot redirect with POSTed data''

    def process_response(self, request, response):
        """ Correct protocols for all href attributes within HTML responses """
        if response[''Content-Type''].find(''html'') >= 0:
            def rewrite_url(match):
                url = match.groups()[0]
                return ''href="%s"'' % self._correct_protocol(request, url)
            try:
                decoded_content = response.content.decode(''utf-8'')
            except UnicodeDecodeError:
                decoded_content = response.content
            response.content = \
                HREF_PATTERN.sub(rewrite_url, decoded_content).encode(''utf-8'')
        return response
