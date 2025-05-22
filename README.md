# EX01 Developing a Simple Webserver
## Date: 21.04.2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```html

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
```
```python
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

```

## OUTPUT:
![alt text](<Screenshot (121).png>)

![alt text](<Screenshot (122).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
