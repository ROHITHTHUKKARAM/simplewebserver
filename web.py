from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Top Software Companies In Revenue With Table</title>
</head>
<body>
<table border="2" cellspacing="5" cellpadding="5" width="40" height="50">
<caption>Top Company Sales sheet</caption>
<tr bgcolor="blue">
<th>Rank</th>
<th>Company</th>
<th>Sales</th>
</tr>

<tr>
<td>1</td>
<td>Microsoft</td>
<td>57.9</td>
</tr>

<tr>
<td>2</td>
<td>Oracle</td>
<td>21.0</td>
</tr>

<tr>
<td>3</td>
<td>SAP</td>
<td>16.1</td>
</tr>

<tr>
<td>4</td>
<td>Adobe</td>
<td>3.4</td>
</tr>

<tr>
<td>5</td>
<td>Electronic Arts</td>
<td>3.2</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()