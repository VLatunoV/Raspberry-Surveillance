# Endpoint for the facebook messenger API
# Not working
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Got post request!")
        self.send_error(404)
        self.end_headers()

class Server(HTTPServer):
    pass

myContext = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH, cafile = None, capath = None, cadata = None)
myContext.options &= ~ssl.OP_NO_SSLv3
myContext.options &= ~ssl.Options.OP_CIPHER_SERVER_PREFERENCE
myServer = Server(('', 27000), Handler)
myServer.socket = myContext.wrap_socket(myServer.socket)
myServer.serve_forever()
