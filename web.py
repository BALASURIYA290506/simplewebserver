from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocols</title>
</head>
<body bgcolor="#121212" text="#ffffff">

    <table width="100%" cellpadding="10">
        <tr>
            <td align="left"><font size="5"><b>Name: Balasuriya M</b></font></td>
            <td align="right"><font size="5"><b>Reg No: 212224240021</b></font></td>
        </tr>
    </table>

    <center>
        <h1>TCP / IP Protocol</h1>
        <table border="1" cellpadding="15" bordercolor="#ffffff" bgcolor="#1e1e1e" width="80%">
            <tr>
                <th><font size="4">TCP/IP LAYER</font></th>
                <th><font size="4">PROTOCOL</font></th>
            </tr>
            <tr>
                <td><font size="3">Application Layer</font></td>
                <td><font size="3">HTTP, HTTPS, FTP, SMTP, DNS, DHCP</font></td>
            </tr>
            <tr>
                <td><font size="3">Transport Layer</font></td>
                <td><font size="3">TCP, UDP</font></td>
            </tr>
            <tr>
                <td><font size="3">Internet Layer</font></td>
                <td><font size="3">IP (IPv4, IPv6), ICMP, ARP, IGMP</font></td>
            </tr>
            <tr>
                <td><font size="3">Network Access Layer</font></td>
                <td><font size="3">Ethernet, Wi-Fi, PPP, SLIP</font></td>
            </tr>
        </table>
    </center>

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