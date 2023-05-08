from fastapi import FastAPI

app = FastAPI()


@app.post("/callback")
async def root(body: dict):
    print(body)
    return "Done"
