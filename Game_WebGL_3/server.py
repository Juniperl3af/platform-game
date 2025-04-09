import http.server
import socketserver
import gzip

PORT = 8000
DIRECTORY = "."  # Current directory

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        if self.path.endswith('.gz'):
            self.send_header('Content-Encoding', 'gzip')

Handler = CustomHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()