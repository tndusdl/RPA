from fastapi import FastAPI
app = FastAPI()

from fastapi import Form
@app.post("/plus")
async def plus_form(num1: int = Form(...), num2 : int = Form(...)):
    result = num1 + num2    
    return {"msg": f"{num1} + {num2} = {result}"}

# if문 위로 항상
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static") 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")