import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/callback", response_class=HTMLResponse)
async def callback(request: Request, body: dict):
    print(body)
    return templates.TemplateResponse("item.html", {"request": request, "body": body})


@app.get('/')
def hello_world():
    print("hello from hello_word")
    return {'message': 'hello'}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request, "id": "adsfasdf"})


if __name__ == "__main__":
    uvicorn.run(app)
