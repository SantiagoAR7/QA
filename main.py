import os
from fastapi import FastAPI
from src.use_cases.clientes import Clientes
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}

@app.get("/clientes")
def get_user():
    return Clientes().get_client("clientes")


if __name__ == "_main_":
    port = int(os.getenv("PORT", 8080))  # Usar la variable PORT que asigna Railway
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)


# uvicorn main:app --host 0.0.0.0 --port 8080