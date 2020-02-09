import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        path = self.path
        print("post")
        if path == "/":       
            length = int(self.headers['content-length'])            
            body = self.rfile.read(length)
            
            # How to convert the body from a string to a dictionary
            # use 'loads' to convert from byte/string to a dictionary!
            dictionary = json.loads(body)
            # To access a specific key from the dictionary:         
            print(dictionary)    
            username = dictionary['username']
            password = dictionary['password']
            self.send_response(200)     
            self.end_headers()
                      
            responseDict = {}            
            responseDict['success'] = True            
            responseDict['otherParams'] = "here"            
            res = json.dumps(responseDict)
            bytesStr = res.encode('utf-8')            
            self.wfile.write(bytesStr)
        else:     
            self.send_response(404)            
            self.end_headers()

    def do_GET(self):
        print("got")
        self.send_response(200)
        self.end_headers()
        self.wfile.write("response body \r\n")

    def do_OPTIONS(self):
        print("options")
        self.send_response(200)
        self.end_headers()

def main():
    # Define the port your server will run on:
    # Using 4001 as an example! Yours may run on another port!
    # Consult with Devops Coordinator to find out which port 
    # your server should be running on!    
    port = 4001
    # Create an http server using the class and port you defined    
    httpServer = http.server.HTTPServer (('', port),SimpleHTTPRequestHandler)    
    print("Running on port", port)
    # this next call is blocking! So consult with Devops Coordinator for
    # instructions on how to run without blocking other commands frombeing
    # executed in your terminal!    
    httpServer.serve_forever()

if __name__ == "__main__":
    main()