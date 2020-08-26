
from joblib import load
from fastapi import FastAPI,Body
import pandas as pd

api_app = FastAPI()

@api_app.post("/predict/")
def predict(
    # description="Measured in mAh"
    battery_power : int = Body(...),

    # description="Has Dual sim support or not"
    dual_sim : int = Body(...),
    
    # description="front camera in MegaPixels"
    front_camera : int = Body(...),

    # description="primary camera in MegaPixels"
    primary_camera : int = Body(...),

    # description="Internal Memory in Gigabytes"
    internal_storage : int = Body(...),

    # description="Number of cores of processor"
    no_of_cores : int = Body(...),

    # description="Random Access Memory in MegaBytes"
    RAM : int = Body(...)
):

    model_file = "/path_where_your_model_saved/test.pkl"
    knn = load(model_file)

    if knn:
        userdata = [{
            'battery_power':battery_power,
            'dual_sim':dual_sim,
            'fc':front_camera,
            'pc':primary_camera,
            'int_memory':internal_storage,
            'n_cores':no_of_cores,
            'ram':RAM
        }]

        userdf = pd.DataFrame(userdata)
        prediction = knn.predict(userdf)

        predicted_cost = str(prediction)
        
        if predicted_cost == "[0]":
            mobile_cost = "Low Cost"
        elif predicted_cost == "[1]":
            mobile_cost = "Medium Cost"
        elif predicted_cost == "[2]":
            mobile_cost = "High Cost"
        elif predicted_cost == "[3]":
            mobile_cost = "Very High Cost"
        else:
            mobile_cost = "Cost not Provided"

    return { "Mobile Cost":str(mobile_cost) }
