# Python Local File Server with 2-way Authentication

This is a simple Python application that sets up a local file server with 2-way authentication using SSL/TLS. It allows you to securely serve files over HTTPS with client authentication.

## Prerequisites

Before using this application, make sure you have the following prerequisites installed:

1. Python 3
2. OpenSSL (for generating certificates)

## Installation

Clone this repository to your local machine.

Generate SSL/TLS certificates for the server and client. You can use OpenSSL or any other method you prefer. Make sure to create the following files:

client.key and client.crt for the client authentication.
ca.crt for the Certificate Authority (CA) certificate.
Replace the placeholder certificates in the repository with your generated certificates.

## Usage
Run the Python server:

python3 server.py
The server will start and listen on all available network interfaces on port 1024 (you can change this in the code).

Access the server via your web browser or a tool that supports HTTPS. You may need to accept the server's certificate when accessing it for the first time.

When prompted, select your client certificate to authenticate yourself. The server will verify your certificate against the CA certificate.

You can now upload or download files securely using the file server.

## Customization
You can customize the following parameters in the code:

Port: You can change the port on which the server listens by modifying the http.server.HTTPServer instantiation.
Security Considerations
Ensure that you keep your certificate files and private keys secure. Do not expose them to unauthorized users.

## License
This project is licensed under the MIT License.

## Disclaimer
This is a basic example for educational purposes. For production use, you should consider more security measures and use a production-ready web server with proper configuration.