from fastapi import FastAPI
app = FastAPI()

from fastapi import File, UploadFile
import shutil
from pathlib import Path

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads")/file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    with save_path("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"filename": file.filename, "location":str(save_path)}

# if문 위로 항상
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static") 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")