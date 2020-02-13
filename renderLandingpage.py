import time
import http.server
from http.server import BaseHTTPRequestHandler
import json

HOST_NAME = "localhost" 
PORT_NUMBER = 8080


# Zoe 2/6/20
# Python application that will ALWAYS be running while the server is up


class PageRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.handle

    def do_GET(self):
        
        path = self.path

        try: 
            """Respond to a GET request."""
            homepage = open("C:\\Users\\Zoe\\Documents\\Spring 2020\\Software Engineering\\Project\\landing\\landing.html", "rb")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(homepage.read())
            homepage.close()

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):

        path = self.path

        if path == "/login":
            loginPage = open("C:\\Users\\Zoe\\Documents\\Spring 2020\\Software Engineering\\Project\\login\\login.html", "rb")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(loginPage.read())
            loginPage.close()

            #self.send_response(200)
            #self.send_header("Content-type", "application/json")
            #self.end_headers()

            #length = int(self.headers['content-length'])
            #body = self.rfile.read(length)
            #dictionary = json.loads(body)
            #print('Username:', dictionary['username'])
            #print("Body:", body)
            #self.send_response(200)

        if path == "/dashboard":
            self.send_header("Content-type", "application/json")
            self.end_headers()

            length = int(self.headers['content-length'])
            body = self.rfile.read(length)
            dictionary = json.loads(body)
            print('Username:', dictionary['username'])
            print("Body:", body)
            self.wfile.write("Entered username: " + dictionary['username'])
            self.wfile.write("Entered password: " + body)
            self.send_response(200)

            dashboardPage = open("C:\\Users\\Zoe\\Documents\\Spring 2020\\Software Engineering\\Project\\dashboard\\dashboard.html", "rb")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(dashboardPage.read())
            dashboardPage.close()

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    httpd = http.server.HTTPServer((HOST_NAME, PORT_NUMBER), PageRequestHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))