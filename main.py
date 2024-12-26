import os
from fastapi import FastAPI, Request
from src.use_cases.clientes import Clientes
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.get("/get_clientes")
async def get_user(request: Request):
    data = await request.json()
    return Clientes().get_client("clientes",data.get("cedula"))

@app.get("/add_clientes")
async def get_user(request: Request):
    data = await request.json()
    return Clientes().add_client(data)


if __name__ == "_main_":
    port = int(os.getenv("PORT", 8080))  # Usar la variable PORT que asigna Railway
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)


# uvicorn main:app --host 0.0.0.0 --port 8080