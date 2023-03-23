import uvicorn
from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List

import time
import logging


import requests 
import magic

logger = logging.getLogger("mycoolapp")

def call_api(url: str, file: UploadFile = File(...)):

    response = requests.post(url, files={'file':file})
    return response

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.post("/uploadfile")
async def create_upload_files(files: List[UploadFile] = File(...)):
    logger.info(f"called JUST upload with {files}")
    contents = []
    time.sleep(5)
    for file in files:
        file_content = await file.read()
        print(file_content, flush=True)
        contents.append(file_content.decode())
    return {"filename": [file.filename for file in files], "contents": contents}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("transcriberx.html", {"request": request})

@app.post("/whisper")
async def upload_file(file: UploadFile = File(...)):
    print("called to write temp file endpoint")
    # Validate that the uploaded file is an audio file
    audio_mime_types = [
        "audio/mpeg",
        "audio/wav",
        "audio/ogg",
        "audio/flac",
        "audio/x-wav",
    ]
    audio_extensions = ["mp3", "wav", "ogg", "flac"]

    # Save uploaded file to a temporary location
    temp_file = f"/tmp/{file.filename}"
    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())

    # cant get this to work without reading the first few bytes of the buffer
    # file_mime_type = magic.from_buffer(temp_file, mime=True)
    file_extension = file.filename.split(".")[-1]
    print(f"file_extension: {file_extension}")
    if file_extension not in audio_extensions: # or  file_mime_type not in audio_mime_types 
        raise HTTPException(status_code=400, detail="File is not an audio file")

    # Call the other API endpoint and pass the file
    url = "http://whisper:5000/whisper"
    # headers = {'Authorization': 'Bearer YOUR_TOKEN'}
    files = {'file': open(temp_file, 'rb')}
    response = requests.post(url, files=files)

    if response.status_code == 200:

        print(response.json())
        return response.json()['results'][0]
    else:
        print(response.status_code)
        print(response.text)
        return {"error": "error"}

@app.get("/upload", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})
