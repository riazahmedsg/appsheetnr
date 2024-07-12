from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# Define a Pydantic model for the input data
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

# Define your machine learning model function
def predict(input_data: InputData) -> float:
    # Here, you would have your actual machine learning model logic
    # For demonstration purposes, let's just return a dummy value
    return input_data.feature1 + input_data.feature2 + input_data.feature3

# Define a route to handle POST requests
@app.post("/predict/")
async def predict_endpoint(input_data: InputData):
    # Call the predict function with the input data
    prediction = predict(input_data)
    return {"prediction": prediction}

# Define a route to handle GET requests
@app.get("/")
    async def read_root():
    return {"message": "Welcome to the ML API and enjoy!"}

# ###########################
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

################################
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# # Assuming you have a function to predict sentiment
# def predict_sentiment(text):
#     # Your machine learning model code goes here
#     # For simplicity, let's just return a dummy sentiment
#     return "positive"
#
# app = FastAPI()
#
# class InputText(BaseModel):
#     text: str
#
# @app.post("/predict")
# def predict(input_text: InputText):
#     text = input_text.text
#     sentiment = predict_sentiment(text)
#     return {"sentiment": sentiment}



