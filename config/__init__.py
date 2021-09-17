import pathlib

ROOT_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = ROOT_DIR.joinpath("data")

API_ADDR = "127.0.0.1"
API_PORT = 1337
API_BASE_URL = "http://{addr}:{port}".format(addr=API_ADDR, port=API_PORT)

MODELS = [
    (
        "/real_estate/predict_price",
        "RealEstateModel",
        str(DATA_DIR.joinpath("real_estate.pkl")),
    ),
    (
        "/vehicle/predict_price",
        "VehicleModel",
        str(DATA_DIR.joinpath("vehicle.pkl")),
    ),
]
MODELS_BY_PATH = {path: (name, pkl_path) for path, name, pkl_path in MODELS}
