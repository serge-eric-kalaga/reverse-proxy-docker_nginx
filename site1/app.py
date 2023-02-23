from fastapi import FastAPI
import  uvicorn

app = FastAPI(debug=True, title="Mon site 1")

@app.get("/app1")
def main():
    return "Mon site 1"


if __name__ == "__main__":
    uvicorn.run("app:app", port=5001, reload=True, host='0.0.0.0')