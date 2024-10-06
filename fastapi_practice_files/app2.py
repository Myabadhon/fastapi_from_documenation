from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/item/{model_name}")
async def read_item(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeNet-based model"}

    return {"model_name": model_name, "message": "Have some residuals"}