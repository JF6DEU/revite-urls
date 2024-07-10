from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import requests
import os

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
template = Jinja2Templates(directory="templates").TemplateResponse

@app.get("/", response_class=HTMLResponse)
async def ytview(request: Request):
response = requests.get(os.environ.get('JSON_URL'))
vm = response.json()
return template("main.html", {brlist:str(vm)});

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
