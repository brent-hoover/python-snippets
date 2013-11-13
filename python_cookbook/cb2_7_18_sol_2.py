import java, javax
class titles(javax.servlet.http.HttpServlet):
    def doGet(self, request, response):
        response.setContentType("text/plain")
        out = response.getOutputStream()
        self.dbQuery(out)
        out.close()
    def dbQuery(self, out):
        driver = "sun.jdbc.odbc.JdbcOdbcDriver"
        java.lang.Class.forName(driver).newInstance()
        # Use "pubs" DB for mssql and "pubs2" for Sybase
        url = "jdbc:odbc:myDataSource"
        usr, passwd = "sa", "password"
        conn = java.sql.DriverManager.getConnection(url, usr, passwd)
        query = "select title, price, ytd_sales, pubdate from titles"
        stmt = conn.createStatement()
        if stmt.execute(query):
            rs = stmt.getResultSet()
            while rs and rs.next():
                out.println(rs.getString("title"))
                if rs.getObject("price"):
                    out.println("%2.2f" % rs.getFloat("price"))
                else:
                    out.println("null")
                if rs.getObject("ytd_sales"):
                    out.println(rs.getInt("ytd_sales"))
                else:
                    out.println("null")
                out.println(rs.getTimestamp("pubdate").toString())
                out.println()
        stmt.close()
        conn.close()
