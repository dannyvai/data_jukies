import SimpleHTTPServer, SocketServer
import urlparse
import os
PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):

       # Parse query data & params to find out what was passed
       parsedParams = urlparse.urlparse(self.path)
       queryParsed = urlparse.parse_qs(parsedParams.query)

       # request is either for a file to be served up or our test
       if parsedParams.path == "/punchin":
          os.system('date >> punch_in.txt')
          self.processMyRequest(queryParsed)
       elif parsedParams.path == "/punchout":
          os.system('date >> punch_out.txt')
          self.processMyRequest(queryParsed)
       else:
          # Default to serve up a local file 
          self.processNotYourBusiness(queryParsed)

   def processMyRequest(self, query):

       self.send_response(200)
       self.send_header('Content-Type', 'application/xml')
       self.end_headers()

       self.wfile.write("<?xml version='1.0'?>");
       self.wfile.write("<sample>It worked!</sample>");
       self.wfile.close();

   def processNotYourBusiness(self, query):

       self.send_response(200)
       self.send_header('Content-Type', 'text/html')
       self.end_headers()

       self.wfile.write("<html>");
       self.wfile.write("<head><title>Button Server</title></head>");
       self.wfile.write("<body>");
       self.wfile.write("<form action=\"punchin\">");
       self.wfile.write("<input type=\"submit\" value=\"punch in\"/><br/>");
       self.wfile.write("</form>");
       self.wfile.write("<form action=\"punchout\">");
       self.wfile.write("<input type=\"submit\" value=\"punch out\"/>");
       self.wfile.write("</form>");
       self.wfile.write("</body>");
       self.wfile.write("</html>");
       self.wfile.close();
Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
