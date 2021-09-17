from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import functools

from config import API_ADDR, API_PORT, MODELS_BY_PATH, DATA_DIR
from model import *  # noqa


@functools.lru_cache(maxsize=None)
def get_cached_model(name, pkl_path) -> PickledModel:
    cls = globals()[name]
    if name == "RealEstateModel":
        obj = cls(
            pkl_path,
            DATA_DIR.joinpath("city.csv"),
        )
    else:
        obj = cls(pkl_path)
    return obj


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
        if self.path not in MODELS_BY_PATH:
            self.send_error(404)
            return

        name, pkl_path = MODELS_BY_PATH[self.path]
        model = get_cached_model(name, pkl_path)
        data = self._recv_json()
        self._send_json(model.predict(data))


def run(server_class=HTTPServer, handler_class=ApiServer, addr="127.0.0.1", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(addr=API_ADDR, port=API_PORT)
