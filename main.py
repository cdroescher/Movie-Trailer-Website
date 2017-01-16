import SocketServer

from connector import MovieConnector
from serverhandler import ServerHandler

PORT = 8000

handler = ServerHandler
handler.movie_connector = MovieConnector()

# start simple python webserver
httpd = SocketServer.TCPServer(("", PORT), handler)
print "serving at port", PORT
httpd.serve_forever()
