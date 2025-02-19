#!/usr/bin/python3
"""
server initialisation
"""
import http.server
import socketserver

PORT = 8000


# classe utilisée pour gérer les requêtes HTTP.
class MyHandler(http.server.BaseHTTPRequestHandler):
    # do_GET qui sera appelée pour traiter les requêtes HTTP GET.
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30,')
            self.wfile.write(b' "city": "New York"}')
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
        # écrit le corps de la réponse, message en texte brut (b=octets)


# On assigne la classe  à la variable Handler.
# Cette variable sera utilisée par le serveur pour gérer les requêtes HTTP.

Handler = MyHandler

# On crée une instance de TCPServer en spécifiant l'adresse
# et le port sur lesquels le serveur écoutera
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    # démarre le serveur et configure pour écouter les requêtes indéfiniment.
    httpd.serve_forever()
