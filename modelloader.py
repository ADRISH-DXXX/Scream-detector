import os
import pandas as pd
from scipy.io.wavfile import read
from tensorflow import keras

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "saved_model")
INPUT_DIM_FILE = os.path.join(BASE_DIR, "input dimension for model.txt")

# load ONCE
model = keras.models.load_model(MODEL_PATH)

with open(INPUT_DIM_FILE, "r") as f:
    INPUT_LEN = int(f.read())


def process_file(filename):
    _, data = read(filename)
    data = data.astype(float)
    data = data[:INPUT_LEN]

    df = pd.DataFrame([data])
    X = df.iloc[:, :INPUT_LEN]

    pred = model.predict(X)
    return round(pred[0][0]) == 1
