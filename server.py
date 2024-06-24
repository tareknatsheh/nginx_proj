from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def main():
    return {"message": "all is good"}


@app.get("/test")
def test_endpoint():
    return {"message": "just a test endpoint"}