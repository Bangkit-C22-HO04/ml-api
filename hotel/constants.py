import os


MODEL_WEIGHT_PATH = os.getenv("MODEL_PATH", "model_data/model_weight")
HOTEL_LIST_PATH = os.getenv("HOTEL_LIST_PATH", "model_data/unique_hotel_id.npy")
TRAVEL_LIST_PATH = os.getenv("HOTEL_LIST_PATH", "model_data/unique_travel_purpose.npy")
