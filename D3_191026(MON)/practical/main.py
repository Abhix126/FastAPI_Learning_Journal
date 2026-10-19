from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Employee Information API",
    description="Day 03 - FastAPI Fundamentals and Basic Routing",
    version="1.0.0"
)


employees = {
    101: {
        "id": 101,
        "name": "Amit",
        "department": "IT",
        "salary": 55000
    },
    102: {
        "id": 102,
        "name": "Priya",
        "department": "HR",
        "salary": 48000
    },
    103: {
        "id": 103,
        "name": "Rahul",
        "department": "IT",
        "salary": 60000
    },
    104: {
        "id": 104,
        "name": "Sneha",
        "department": "Finance",
        "salary": 52000
    }
}


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Information API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "application": "Employee Information API",
        "framework": "FastAPI",
        "language": "Python",
        "day": 3,
        "version": "1.0.0"
    }


@app.get("/employees")
def get_employees(department: str | None = None):

    employee_list = list(employees.values())

    if department is not None:
        employee_list = [
            employee
            for employee in employee_list
            if employee["department"].lower() == department.lower()
        ]

    return {
        "total": len(employee_list),
        "employees": employee_list
    }


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    employee = employees.get(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )