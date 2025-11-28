from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI in Kubernetes!"}
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}
