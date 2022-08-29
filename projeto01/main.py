import imp
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def raiz():
    return {"msg": "FastAPI dale dale"}




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, log_level="info", reload=True)
