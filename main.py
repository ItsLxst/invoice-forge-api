from fastapi import FastAPI
import uvicorn
from app.routers.invoices import router

# run like flask settings
HOST = "127.0.0.1"
PORT = 8000
APP_PATH = "main:app"  # app object in main file

app = FastAPI()
app.include_router(router, prefix="/invoices")

@app.get("/")
def root():
    return {"message": "Invoice Forge API is running"}

# run like flask
if __name__ == "__main__":
  uvicorn.run(APP_PATH, host=HOST, port=PORT, reload=True)
