from fastapi import FastAPI, Form, File, UploadFile 
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO
from fastapi.staticfiles import StaticFiles
import qrcode.constants

app = FastAPI()

@app.get("/files/{filename}")
async def get_file(filename: str):
    file_path = Path("static/uploads") / filename

    if file_path.is_file():
        return FileResponse(path=file_path, filename=filename)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.post("/qrcode/")
async def generate_qr(data:str = Form(...)):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color ='white')
    
    # 바이너리 데이터로 변환
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr), media_type="image")
    
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "location": str(save_path)}


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
