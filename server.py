from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head><title>Minimal server</title></head>
        <body>
            <h1>Hello World</h1>
            <p>Your server is working.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))


server = HTTPServer(("0.0.0.0", 80), Handler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
