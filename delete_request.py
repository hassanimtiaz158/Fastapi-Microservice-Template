from dataclasses import field
import json
from fastapi.background import P
from pydantic import BaseModel,Field, HttpUrl,computed_field
from typing import Annotated,Literal,Optional
from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse


class Patient(BaseModel):

    patient_id: Annotated[str,Field(...,description="Add ID of the patient")]
    name: Annotated[str,Field(...,description="Add name of the patient")]
    age: Annotated[int,Field(...,gt=0,lt=120,description="Add age of the parient")]
    gender: Annotated[Literal["Male","Female","Others"],Field(...,description="Gender of the patient")]
    height: Annotated[float,Field(...,gt=0,description="Height of the patient")]
    weight: Annotated[float,Field(...,gt=0,description="Weight of the patient")]
    

    @computed_field
    @property
    def bmi(self)-> float:
        bmi=(self.weight)/(self.height**2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18:
            return "underweight"
        elif self.bmi<25:
            return "normal"
        elif self.bmi<30:
            return "A-normal"
        elif self.bmi<50:
            return "overweight"
        else:
            return "obeese"
        
class Patient_update(BaseModel):

    name: Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int],Field(default=None,gt=0,lt=120)]
    gender: Annotated[Optional[Literal["Male","Female","Others"]],Field(default=None)]
    height: Annotated[Optional[float],Field(default=None,gt=0)]
    weight: Annotated[Optional[float],Field(default=None,gt=0)]

            

app=FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
    return data

def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {"message":"hello,world"}

@app.get("/view")
def view():
    data=load_data()
    return data

@app.get("/about")
def about():
    return {"message":"this apis is for practice"}

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(...,description="This is for patient_ID",
                                      example="like P001 etc")):
    data=load_data()

    for id in data:
        if id==patient_id:
            return data[id]
        
    raise HTTPException(status_code=404,detail="Patient not found!")

@app.get("/sort")
def sort(sort_by:str=Query(...,description="Sort on the basis of height,weight or bmi"),
         order:str=Query("asc",description="order by asc or desc")):
    
    data=load_data()

    sort_method=["height","weight","bmi"]
    if sort_by not in sort_method:
        raise HTTPException(status_code=400,detail=f"Bad request, select from {sort_method}")

    order_method=["asc","desc"]
    if order not in order_method:
        raise HTTPException(status_code=400,detail=f"Bad Request, select from {order_method}")
    
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0), reverse=sort_order)
    
    return sorted_data

@app.post("/create")
def create_patient(patient: Patient):
    data=load_data()
    if patient.patient_id in data:
        raise HTTPException(status_code=400,detail="Patient with this id exist")
    
    data[patient.patient_id]=patient.model_dump(exclude="patient_id")

    save_data(data)
    return JSONResponse(status_code=201,content={"message": "Patient created successfully"})


@app.put("/edit/{patient_id}")
def update_patient_function(patient_id: str, update_patient: Patient_update):
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=400,detail="Patient not exists")
    
    existing_info=data[patient_id]
    updating_info=update_patient.model_dump(exclude_unset=True)

    for key,value in updating_info.items():
        existing_info[key]=value

    existing_info['patient_id']=patient_id
    updated_patient_pydantic_object=Patient(**existing_info)

    existing_info=updated_patient_pydantic_object.model_dump(exclude='patient_id')

    data[patient_id]=existing_info

    save_data(data)

    return JSONResponse(status_code=200,content={"message":"Patient updated successfully!"})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=400,detail="Patient not exists")
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={"message":"Patient deleted successfully!"})