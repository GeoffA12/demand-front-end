import time
import http.server
from http.server import BaseHTTPRequestHandler
import json

HOST_NAME = "localhost" 
PORT_NUMBER = 8080


class HomePageHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        path = self.path
        try: 
            """Respond to a GET request."""
            homepage = open("C:\\Users\\Zoe\\Documents\\Spring 2020\\Software Engineering\\Project\\landingpage\\team22se.html", "rb")
            img_pharmacy = open("C:\\Users\\Zoe\\Documents\\Spring 2020\\Software Engineering\\webpage\\note.png", "rb")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(homepage.read())
            homepage.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
    def do_POST(self):
        path = self.path
        print("I was called with a POST request")
        if path == "/loginPage":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            length = int(self.headers['content-length'])
            body = self.rfile.read(length)
            dictionary = json.loads(body)
            print('Username:', dictionary['username'])
            print("Body:", body)
            self.send_response(200)
        else:
            self.send_response(404)
            self.end_headers()
    
   
if __name__ == '__main__':
    httpd = http.server.HTTPServer((HOST_NAME, PORT_NUMBER), HomePageHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))