#!/usr/bin/python3
"""
server initialisation
"""
import http.server
import socketserver
import json

PORT = 8000


# classe utilisée pour gérer les requêtes HTTP.
class SubclassHandler(http.server.BaseHTTPRequestHandler):
    # do_GET qui sera appelée pour traiter les requêtes HTTP GET.
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            # info API
            data = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
        # écrit le corps de la réponse, message en texte brut (b=octets)


# On crée une instance de TCPServer en spécifiant l'adresse
# et le port sur lesquels le serveur écoutera
with socketserver.TCPServer(("", PORT), SubclassHandler) as httpd:
    print("serving at port", PORT)
    # démarre le serveur et configure pour écouter les requêtes indéfiniment.
    httpd.serve_forever()
