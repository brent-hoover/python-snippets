import java, javax
class goosebumps(javax.servlet.http.HttpServlet):
    def doGet(self, request, response):
        response.setContentType("text/plain")
        out = response.getOutputStream()
        self.dbQuery(out)
        out.close()
    def dbQuery(self, out):
        driver = "org.gjt.mm.mysql.Driver"
        java.lang.Class.forName(driver).newInstance()
        server, db = "server", "test"
        usr, passwd = "root", "password"
        url = "jdbc:mysql://%s/%s?user=%s&password=%s" % (
            server, db, usr, passwd)
        conn = java.sql.DriverManager.getConnection(url)
        query = "select country, monster from goosebumps"
        stmt = conn.createStatement()
        if stmt.execute(query):
            rs = stmt.getResultSet()
            while rs and rs.next():
                out.println(rs.getString("country"))
                out.println(rs.getString("monster"))
                out.println()
        stmt.close()
