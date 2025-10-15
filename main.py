from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import json, jsonpickle

app = FastAPI()

class Student(BaseModel):
    name: str
    rollNo: int
    marks: list[int]
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__)

@app.get("/")
def example():
    return {1:"First Example"}

@app.get("/get_all/")
async def get_all():
    try:
        with open("student_details.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        return []
    return data

@app.get("/get_average/")
async def get_average():
    data = await get_all()
    return {
        "average": 
            sum(
                [
                    sum([marks for marks in student["marks"]])
                    /len(student["marks"]) 
                    for student in data
                ]
            )/len(data)
    }

@app.post("/add/")
async def add(request: Request):
    request = await request.json()

    try: 
        request = Student(**request)
    except Exception as e: 
        raise HTTPException(status_code = 400, detail = "Bad request. Does not match class schema")

    request = jsonpickle.decode(request.toJSON())

    data = await get_all()
    for student in data:
        if student["rollNo"] == request["rollNo"]:
            raise HTTPException(status_code = 409, detail = "Student already exists")
    else:
        data.append(request)
    with open("student_details.json", "w") as f: json.dump(data, f, indent = 4)
    return {"status": "success"}
