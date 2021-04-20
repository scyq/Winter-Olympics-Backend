import sys

sys.path.append("./yolo")
import os
from fastapi.responses import JSONResponse, FileResponse
from draw.draw import draw
from demo import detect_curling
from fastapi import FastAPI

app = FastAPI()
headers = {"Access-Control-Allow-Origin": "*"}


# 返回画完后的图像
@app.get("/start")
async def start():
    try:
        detect_curling(
            "./yolo/data/1.mp4", "./yolo/data/coordinates.txt"
        )
        draw()
    except:
        return JSONResponse(False, headers=headers)
    return FileResponse("./output/frame.jpg", headers=headers)


@app.get("/vr")
def vr():
    os.system('''conda.bat activate "C:\Anaconda3"&\
                              python C:/Users/887/Desktop/temp/test3.py --url wss://kirnu-ws2.stereye.tech --password kirnu&''')
    return JSONResponse(False, headers=headers)
