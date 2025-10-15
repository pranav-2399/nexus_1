# 🧠 FastAPI Student Details Backend

The repository contains a simple **Python backend** built with **uvicorn**, **FastAPI** and tested using **Postman**.  
The data is stored in an array of JSON objects inside the file **`student_details.json`**.

To run `main.py`:

   ```python
   uvicorn main:app --reload
   ```

   ```python
   class Student(BaseModel):
       roll_no: int
       name: str
       marks: list[int]
   ```

## 📄 `main.py`

This file defines **three API endpoints:**

- `get_all`  
- `get_average`  
- `add`

### 🟦 `/get_all` Endpoint

Retrieves all the student records from **`student_details.json`**.
   ```python
      @app.get("/get_all/")
      async def get_all():
           with open("student_details.json", "r") as f: data = json.load(f)
          return data
   ```

### 🟩 `/get_average` Endpoint

Computes the average marks for each student, based on their scores stored in the file.
   ```python
      @app.get("/get_average/")
      async def get_average():
          data = await get_all()
          return { "average": <Average of every student's average marks>}
   ```

## 🟥 `/add` Endpoint

Accepts a new student object matching the schema of the **`Student`** class (defined in the same file).  
If the schema does not match, it throws a **400 Bad Request** error.  
If the roll number already exists, it throws a **409 Conflict** error.  
If successful, it appends the object to **`student_details.json`** and saves it.
   ```python
      @app.post("/add/")
      async def add(request: Request):
          try: request = Student(**request)
          except Exception as e: raise HTTPException(status_code = 400)      
          data = await get_all()
          for student in data: if student["rollNo"] == request["rollNo"]: raise HTTPException(status_code = 409)
          else: data.append(request)
          with open("student_details.json", "w") as f: json.dump(data, f, indent = 4)
   ```

