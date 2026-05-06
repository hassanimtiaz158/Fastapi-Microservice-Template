from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict_model import ML_MODEL_VERSION, predict_output
from schema.output_response import PredictionResponse

app=FastAPI()

@app.get("/")
def home():
    return  {"message":"Welcome To our Model Prediction API"}

@app.get("/health")
def health_check():
    return {
        "message":"All Good!",
        "status":"OK",
        "MODEL":"Running"
    }

@app.get("/version")
def model_version():
    return {"MODEL VERSION":ML_MODEL_VERSION}

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        predict=predict_output(user_input)
        return JSONResponse(status_code=200, content={"Prediction_Category":predict})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))


