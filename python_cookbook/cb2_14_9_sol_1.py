import java, javax, sys
class hello(javax.servlet.http.HttpServlet):
    def doGet(self, request, response):
        response.setContentType("text/html")
        out = response.getOutputStream()
        print >>out, """<html>
<head><title>Hello World</title></head>
<body>Hello World from Jython Servlet at %s!
</body>
</html>
""" % (java.util.Date(),)
        out.close()
        return
