import time

import BaseHTTPServer

HOST_NAME = '172.17.56.9' # !!!REMEMBER TO CHANGE THIS!!!

PORT_NUMBER = 80 # Maybe set this to 9000.

a=0

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

def do_HEAD(s):

s.send_response(200)

s.send_header("Content-type", "text/html")

s.end_headers()

def do_GET(s):

dados = le_dados()

print (dados)

"""Respond to a GET request."""

if s.path=="/1":

s.send_response(200)

s.send_header("Content-type", "text/plain")

s.end_headers()

s.wfile.write(dados)

elif s.path=="/2":

s.send_response(200)

s.send_header("Content-type", "text/plain")

s.end_headers()

s.wfile.write("2")

else:

s.send_response(200)

s.send_header("Content-type", "text/plain")

s.end_headers()

s.wfile.write(dados)

def le_dados():

arq = open('/tmp/dados.txt', 'r')

texto = arq.readline()

arq.close()

return texto

if _name_ == '_main_':

server_class = BaseHTTPServer.HTTPServer

httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)

print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)

try:

a=a+2

httpd.serve_forever()

except KeyboardInterrupt:

pass

httpd.server_close()

print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

Código de Execução dos Códigos anteriores no Shell

echo "starting mag_python"

sudo python mag_python.py &

echo "start server"

sudo python server2.py
