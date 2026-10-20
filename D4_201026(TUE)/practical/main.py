from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, ConfigDict


app = FastAPI(
    title="Employee Registration API",
    description="Day 04 - Pydantic Models, Request Bodies and Data Validation",
    version="1.0.0"
)


# --------------------------------------------------
# Pydantic Models
# --------------------------------------------------

class EmployeeCreate(BaseModel):

    model_config = ConfigDict(extra="forbid")

    name: str = Field(
        min_length=2,
        max_length=50
    )

    department: str = Field(
        min_length=2,
        max_length=50
    )

    salary: float = Field(
        gt=0,
        allow_inf_nan=False
    )

    age: int = Field(
        ge=18,
        le=65,
        strict=True
    )

    email: str | None = None

    is_active: bool = True


class EmployeeResponse(BaseModel):

    id: int
    name: str
    department: str
    age: int
    email: str | None
    is_active: bool


# --------------------------------------------------
# In-Memory Data Store
# --------------------------------------------------

employees = {
    101: {
        "id": 101,
        "name": "Amit",
        "department": "IT",
        "salary": 55000.0,
        "age": 25,
        "email": "amit@example.com",
        "is_active": True
    },
    102: {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 48000.0,
        "age": 27,
        "email": None,
        "is_active": True
    }
}

next_employee_id = 103


# --------------------------------------------------
# Basic Endpoints
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Welcome to Employee Registration API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Register Employee
# --------------------------------------------------

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee: EmployeeCreate):

    global next_employee_id

    employee_id = next_employee_id
    next_employee_id += 1

    employee_data = employee.model_dump()

    employee_data["id"] = employee_id

    employees[employee_id] = employee_data

    return employee_data


# --------------------------------------------------
# Retrieve All Employees
# --------------------------------------------------

@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_employees():

    return list(employees.values())


# --------------------------------------------------
# Retrieve Employee by ID
# --------------------------------------------------

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(employee_id: int):

    employee = employees.get(employee_id)

    if employee is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return employee


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )