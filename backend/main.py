from fastapi import FastAPI

app = FastAPI(
    title="Food Recommendation API",
    version="1.0.0",
)


@app.get("/api/test")
def test_api():
    return {"test": "GET success"}