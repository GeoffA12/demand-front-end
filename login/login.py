import http.server
from http.server import BaseHTTPRequestHandler
import jsonimport 
import urllib.parseclassSimple


class team22HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        post = self.path
        
        if path == "/":
            # You can get all headers via self.headers
            # or identify which header you want to get
            print('Headers:"', self.headers, '"')            
            print('Content-Type:', self.headers['content-type'])
            # This is how you read the body of the request:
            # First grab the length of the body and read# that many characters            
            length = int(self.headers['content-length'])            
            body = self.rfile.read(length)
            # at this point you can print the whole body 
            # if you want (good for debugging) 
            # at this point body is in bytes            
            print('Body:', body) # convert bytes to string using .decode()
            print("Body (String): ", body.decode())
            
            # How to convert the body from a string to a dictionary
            # use 'loads' to convert from byte/string to a dictionary!
            dictionary = json.loads(body)
            # To access a specific key from the dictionary:             
            print('Username:', dictionary['username'])
            # Now you can get to the important stuff (DB, API calls, etc)
            # If you need to make API calls use the python 'requests'library -> https://requests.readthedocs.io/en/master/
            # For connecting to a MySQL DB, use 'pymysql' library ->https://pymysql.readthedocs.io/en/latest/
            # For connecting to MongoDB, use 'pymongo' library ->https://api.mongodb.com/python/current/
            # Now send a response code!
            # For a comprehensive list of response codes and what theymean, see -> https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
            # If everything went well, send a 200!            
            self.send_response(200)
            # Very important, or your response will be slow!
            # Signify that you are done sending headers            
            self.end_headers()
            # There are a few ways to send a response
            # If you don't want to format your JSON, make a dictionary,and 
            # convert it to a string with 'json.dumps'            
            responseDict = {}            
            responseDict['success'] = True            
            responseDict['otherParams'] = "here"            
            res = json.dumps(responseDict)
            # Whichever way you choose, you need to have a string that youcan convert to bytes because the body only receives bytes.            
            bytesStr = res.encode('utf-8')            
            self.wfile.write(bytesStr)
            # Check as many paths as you have POST requests
        else: 
            # if the path did not match any of 
            # your known requests return a 404 Not Found            
            self.send_response(404)            
            self.end_headers()

    def do_GET(self):
        print("got")
    
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