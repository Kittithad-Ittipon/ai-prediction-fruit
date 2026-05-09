from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from joblib import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
model = load("fruit_model.pkl")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    size = float(data.get("size", 0))
    shape = int(data.get("shape", 0))
    weight = float(data.get("weight", 0))
    color = int(data.get("color", 0))
    taste = int(data.get("taste", 0))
    features = np.array([[size, shape, weight, color, taste]])
    prediction = model.predict(features)[0]
    fruit_names = {
        14: "pear", 17: "pomegranate", 15: "pineapple", 5: "custard apple",
        13: "papaya", 9: "kiwi", 2: "blueberry", 1: "banana",
        4: "coconut", 10: "lychee", 11: "mango", 7: "grape",
        19: "watermelon", 6: "dragon fruit", 0: "apple", 16: "plum",
        12: "orange", 8: "guava", 3: "cherry", 18: "strawberry"
    }
    fruit_name = fruit_names.get(prediction, "Unknown")
    return {"fruit": fruit_name, "img_url": f"/static/{fruit_name}.png"}