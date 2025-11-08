from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.get("/hello")
def hello():
    return {"message": "Hello world"}


@app.get("/stats")
def stats():
    return {"message": "Aqui veras las estadisticas"}


@app.get("/graf")
def stats():
    return {"message": "Aqui veras las graficas"}
