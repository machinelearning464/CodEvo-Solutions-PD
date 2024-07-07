import png
import http.server
import socket
import socketserver
import pyqrcode
from pyqrcode import QRCode 
import webbrowser
import os
port =8010
str1 =os.environ['USERPROFILE'] #for getting the name of user
desktop=os.path.join(os.path.join(str1),'OneDrive')
os.chdir(desktop)
handler=http.server.SimpleHTTPRequestHandler
host=socket.gethostname()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
IP="http://"+s.getsockname()[0]+":"+str(port)
link=IP
url=pyqrcode.create(link)
url.svg("myqr.svg",scale=8)
webbrowser.open('myqr.svg')
with socketserver.TCPServer(("",port),handler) as httpd:
    print("currently serving on the port number",port)
    print("You can share file using any one of following methods")
    print("1.Enter the given ip address in your browser: ",IP)
    print("2.Scan the given QR code")
    httpd.serve_forever()