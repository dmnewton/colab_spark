import socketserver
from http.server import SimpleHTTPRequestHandler
import urllib.request
PORT = 9090
class MyProxy(SimpleHTTPRequestHandler):
  def do_GET(self):
    url=self.path[1:]
    url="http://localhost:4040/" + url
    resp=urllib.request.urlopen(url)
    self.send_response(200)
    self.send_header("Content-type", resp.headers.get_content_type())
    self.end_headers()
    self.copyfile(resp, self.wfile)
httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print ("Now serving at",str(PORT))
httpd.serve_forever()