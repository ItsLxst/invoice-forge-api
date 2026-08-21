from fastapi import FastAPI
import uvicorn


# run like flask settings
HOST = "127.0.0.1"
PORT = 8000
APP_PATH = "main:app"  # app object in main file

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}


# run like flask
if __name__ == "__main__":
  uvicorn.run(APP_PATH, host=HOST, port=PORT, reload=True)