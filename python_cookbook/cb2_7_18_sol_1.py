import java, javax
class emp(javax.servlet.http.HttpServlet):
    def doGet(self, request, response):
        ''' a Servlet answers a Get query by writing to the response's
            output stream.  In this case we ignore the request, though
            in normal, non-toy cases that's where we get form input from.
        '''
        # we answer in plain text, so set the content type accordingly
        response.setContentType("text/plain")
        # get the output stream, use it for the query, then close it
        out = response.getOutputStream()
        self.dbQuery(out)
        out.close()
    def dbQuery(self, out):
        # connect to the Oracle driver, building an instance of it
        driver = "oracle.jdbc.driver.OracleDriver"
        java.lang.Class.forName(driver).newInstance()
        # get a connection to the Oracle driver w/given user and password
        server, db = "server", "ORCL"
        url = "jdbc:oracle:thin:@" + server + ":" + db
        usr, passwd = "scott", "tiger"
        conn = java.sql.DriverManager.getConnection(url, usr, passwd)
        # send an SQL query to the connection
        query = "SELECT EMPNO, ENAME, JOB FROM EMP"
        stmt = conn.createStatement()
        if stmt.execute(query):
            # get query results and print the out to the out stream
            rs = stmt.getResultSet()
            while rs and rs.next():
                out.println(rs.getString("EMPNO"))
                out.println(rs.getString("ENAME"))
                out.println(rs.getString("JOB"))
                out.println()
        stmt.close()
        conn.close()
