from fastapi import FastAPI,HTTPException,Body 

app = FastAPI()


@app.post("/registration")
def registration (name:str= Body(), age:int=Body() , vet:bool=Body(), retired: bool=Body()) : 
    if age<65:
        raise  HTTPException(status_code=400,detail="Age must be 65 or above")
    return {"Status" :"Qualified for Veteran's Program"}


#Directions --> open two terminals in VS code

# in one terminal, run uvicorn  postMethod:app --reload  

#in the other terminal, run these two test cases 
#two test cases

# curl -X POST "http://127.0.0.1:8000/registration" -H "Content-Type: application/json" -d '{"name": "james", "age": 64, "vet": true, "retired": true}' 

# curl -X POST "http://127.0.0.1:8000/registration" -H "Content-Type: application/json" -d '{"name": "james", "age": 70, "vet": true, "retired": true}'