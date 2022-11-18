from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    a: int
    b: int

@app.get("/")
async def welcome():
    return {
        'message': 'welcome to math lab'
    }

@app.post("/addition")
async def addition(data: Data):
    solution = addition_function(data.a, data.b)
    return solution

def addition_function(a, b):
    return a + b

