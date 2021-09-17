import pathlib

ROOT_DIR = pathlib.Path(__file__).parent
PICKLES_DIR = ROOT_DIR.joinpath("pickles")

API_ADDR = "127.0.0.1"
API_PORT = 1337
API_BASE_URL = "http://{addr}:{port}".format(addr=API_ADDR, port=API_PORT)

MODELS = [
    (
        "/real_estate/predict_price",
        "RealEstateModel",
        str(PICKLES_DIR.joinpath("real_estate.v2.pkl")),
    ),
    (
        "/vehicle/predict_price",
        "VehicleModel",
        str(PICKLES_DIR.joinpath("vehicle.v3.pkl")),
    ),
]
