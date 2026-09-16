from fastapi import FastAPI, Body, Form, UploadFile, File
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    in_stock : bool

@app.post("/json")
def recieve_json(item: Item):
    return{
        "type" : "json",
        "name" : item.name,
        "price" : item.price,
        "in_stock" : item.in_stock
    }

@app.post("/text")
def recieve_text(data: str = Body(..., media_type="text/plain")):
    return{
        "type" : "text",
        "data" : data
    }

@app.post("/form")
def recieve_form(username: str = Form(...), password: str = Form(...)):
    return {
        "type" : "form data",
        "username" : username,
        "password" : password    
    }

@app.post("/uploadfile")
def upload_file(file:UploadFile = File(...)):
    return {
        "type" : "file upload",
        "filename" : file.filename,
        "content_type" : file.content_type
    }