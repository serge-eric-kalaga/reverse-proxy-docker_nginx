from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True, title="Mon site 2")

@app.get("/app2")
def main():
    return "Mon site 2"


if __name__ == "__main__":
    uvicorn.run("app:app", port=5002, reload=True, host='0.0.0.0')