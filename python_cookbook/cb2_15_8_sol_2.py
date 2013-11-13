import sys, os
import CORBA, Fortune, Fortune__POA
FORTUNE_PATH = "/usr/games/fortune"
class CookieServer_i(Fortune__POA.CookieServer):
    def get_cookie(self):
        pipe   = os.popen(FORTUNE_PATH)
        cookie = pipe.read()
        if pipe.close():
            # An error occurred with the pipe
            cookie = "Oh dear, couldn't get a fortune\n"
        return cookie
orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")
servant = CookieServer_i()
poa.activate_object(servant)
print orb.object_to_string(servant._this())
# see the Discussion session about what this print statement emits
poa._get_the_POAManager().activate()
orb.run()
