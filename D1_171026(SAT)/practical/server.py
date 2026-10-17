from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status_code=200):
        """Send a JSON response with the appropriate HTTP status and headers."""

        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):
        """Handle incoming HTTP GET requests."""

        print("Request received:", self.path)

        if self.path == "/":
            self.send_json({
                "message": "Welcome to Daily FastAPI Practice"
            })

        elif self.path == "/health":
            self.send_json({
                "status": "healthy"
            })

        elif self.path == "/info":
            self.send_json({
                "application": "Local HTTP API",
                "language": "Python",
                "day": 1
            })

        else:
            self.send_json({
                "error": "Endpoint not found"
            }, status_code=404)


if __name__ == "__main__":

    HOST = "127.0.0.1"
    PORT = 8000

    server = HTTPServer((HOST, PORT), APIHandler)

    print(f"Server running at http://{HOST}:{PORT}")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nStopping server...")

    finally:
        server.server_close()
        print("Server stopped successfully.")