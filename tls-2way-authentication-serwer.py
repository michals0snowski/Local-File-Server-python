import http.server, ssl

def handler(*args, **kwargs):
    http.server.SimpleHTTPRequestHandler(*args, **kwargs)

httpd = http.server.HTTPServer(("0.0.0.0", 1024), handler) # without sudo only ports above 1024
httpd.socket = ssl.wrap_socket(httpd.socket, 
    keyfile="path/to/keyfile.key",
    certfile="path/to/certificate.crt",
    server_side=True,
    ssl_version=ssl.PROTOCOL_TLSv1_2,
    ca_certs="path/to/ca.crt",
    cert_reqs=ssl.CERT_OPTIONAL # or ssl.CERT_REQUIRED
)
httpd.serve_forever()