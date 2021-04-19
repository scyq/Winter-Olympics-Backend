from fastapi import FastAPI
from yolo.demo import detect_curling
from draw.draw import draw
from fastapi.responses import JSONResponse
import os

app = FastAPI()
headers = {"Access-Control-Allow-Origin": "*"}


# 返回画完后的图像
@app.get("/start")
def start():
    try:
        detect_curling(
            "./yolo/data/1.mp4", "./yolo/data/coordinates.txt"
        )
        draw()
    except:
        return False
    return JSONResponse(True, headers=headers)
