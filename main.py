from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse,JSONResponse
from bk import process_doodstream_url
app = FastAPI()

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

# Serve static files if needed (optional)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/fetch-link")
async def fetch_link(request: Request):
    data = await request.json()
    url = data.get("url")
    result = process_doodstream_url(url)
    return JSONResponse({"result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
