from fastapi import FastAPI
app = FastAPI()

from fastapi import Form
@app.post("/plus2")
async def plus_form(num1: int = Form(...), num2 : int = Form(...), num3: int = Form(...), num4 : int = Form(...)):
    result1 = num1 + num2    
    result2 = num3 + num4    
    return {"result": f"{num1} + {num2} = {result1} | {num3} + {num4} = {result2}"}

# if문 위로 항상
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static") 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")