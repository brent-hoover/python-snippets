from java import lang, sql
lang.Class.forName('sun.jdbc.odbc.JdbcOdbcDriver')
excel_file = 'values.xls'
connection = sql.DriverManager.getConnection(
    'jdbc:odbc:Driver={Microsoft Excel Driver (*.xls)};DBQ=%s;READONLY=true}' %
    excelfile, '', '')
# Sheet1 is the name of the Excel workbook we want.  The field names for the
# query are implicitly set by the values for each column in the first row.
record_set = connection.createStatement().executeQuery(
             'SELECT * FROM [Sheet1$]')
# print the first-column field of every record (==row)
while record_set.next():
    print record_set.getString(1)
# we're done, close the connection and recordset
record_set.close()
connection.close()
