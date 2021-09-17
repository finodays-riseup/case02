from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from config import API_ADDR, API_PORT


class ApiServer(BaseHTTPRequestHandler):
    def _recv_json(self) -> bytes:
        b = self.rfile.read(int(self.headers.get("content-length", 0)))
        s = b.decode("utf-8")
        obj = json.loads(s)

        return obj

    def _send_json(self, data):
        s = json.dumps(data)
        b = s.encode("utf-8")

        self.send_response(200)
        self.send_header("content-length", str(len(b)))
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(b)

    def do_POST(self):
        if self.path == "/real_estate/predict_price":
            self._send_json({"price": 123456})
        elif self.path == "/vehicle/predict_price":
            self._send_json({"price": 654321})
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=ApiServer, addr="127.0.0.1", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(addr=API_ADDR, port=API_PORT)
