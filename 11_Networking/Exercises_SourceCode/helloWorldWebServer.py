#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A Web server that just says "Hello World."'''

__author__ = 'Russel Winder'
__date__ = '2012-08-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer  # Python 3
    version = 3
except:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  # Python 2
    version =2

class HelloWorldHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Get request from {}'.format(self.client_address))
        response = '''HTTP/1.0 200 OK
Content-type: text/html

<h1>Hello World.</h1>'''
        if version == 3:
            response = response.encode()
        self.wfile.write(response)

if __name__ == '__main__':
    port = 8001
    server = HTTPServer(('', port), HelloWorldHTTPRequestHandler)
    print('Serving on port {}'.format(port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
