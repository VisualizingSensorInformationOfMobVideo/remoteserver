#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import cgi
import datetime

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><head><title>VSD</title></head><body><h1>VisualizingSensorData</h1><p>See <a href=\"https://github.com/VisualizingSensorInformationOfMobVideo/VisualizingSensorData\">https://github.com/VisualizingSensorInformationOfMobVideo/VisualizingSensorData</a></body></html>\n")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

        if ctype != 'text/xml':
            print "Missing XML content-type."
            self._set_headers()
            self.wfile.write("I want XML-data (and content-type)!\n")
            return

        length = int(self.headers.getheader('content-length'))
        data = self.rfile.read(length)

        if data == "":
            self._set_headers()
            self.wfile.write("Missing data!\n")
        else:
            # store a new file
            path = datetime.datetime.now().strftime("output/%Y-%m-%d.%H%M%S.%f.xml");
            with open(path, "w") as fp:
                fp.write(data)

            self._set_headers()
            self.wfile.write("Data retrieved succesfully!\n")
        
def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
