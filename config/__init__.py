API_ADDR = "127.0.0.1"
API_PORT = 1337
API_BASE_URL = "http://{addr}:{port}".format(addr=API_ADDR, port=API_PORT)

MODELS = [
    ("/real_estate/predict_price", "RealEstateModel", ""),
    ("/vehicle/predict_price", "VehicleModel", ""),
]
