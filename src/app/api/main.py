from fastapi import FastAPI

app = FastAPI(title="AI Personal Communication Assistant API")


@app.get("/")
def health_check():
    return {"status": "running", "application": "AI Personal Communication Assistant"}
