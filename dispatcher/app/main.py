from fastapi import FastAPI

app = FastAPI(title="Dispatcher Service")

@app.get("/")
def root():
    return {"message": "Dispatcher service is running"}
    