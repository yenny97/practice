#--------------Library----------------
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
#--------------------------------------

app = FastAPI() 

app.mount("/static",StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='static')

@app.get('/form_test',response_class=HTMLResponse)
def read_html(request : Request):
    return templates.TemplateResponse("test.html",{"request": request})


@app.post('/login')
def test_login(id : str = Form(...),
               password: str = Form(...)):
                   print(id,password)
                   return 0


@app.get("/") 
def root():
    return {'message' : 'hello world'} 
    

@app.post('/py')
def root():
    def post_test():
        return{'message': 'hi'}


@app.get('/serial/{serial}')
def dynamic_test(serial : int):
    return serial


@app.get('/get_items')
def read_items(start:int=0 , end:int=1):
    return fake_items[start:start+end]

fake_items = [{"item_name":'hello'}],[{"item_name":'hi'}]


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= 'localhost',
        port=3000,
        reload=True,

    )