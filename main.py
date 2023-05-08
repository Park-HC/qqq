import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
async def root(body: dict):
    print(body)
    return "Done"

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=5010)
