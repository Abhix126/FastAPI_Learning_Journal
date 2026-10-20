# Day 04 — Pydantic Models, Request Bodies & Data Validation

**Date:** 20 October 2026 (Tuesday)  
**Learning Track:** Daily REST API & FastAPI Practice  
**Topic:** Pydantic Models, JSON Request Bodies, Field Validation & Response Models  
**Tools:** Python 3.12, PyCharm, FastAPI, Pydantic, Uvicorn, Postman  
**Level:** Beginner

---

## 1. Learning Objectives

- Understand Pydantic and its role in FastAPI.
- Define structured data models using `BaseModel`.
- Accept JSON request bodies.
- Understand required, optional, and default fields.
- Apply field constraints using `Field()`.
- Implement POST endpoints with request validation.
- Define response models using `response_model`.
- Understand automatic validation errors.

---

## 2. Introduction to Pydantic

**Pydantic** is a Python library used for data validation, serialization, and defining structured data models using type annotations.

FastAPI integrates Pydantic to validate incoming request data.

### Key Features

| Feature | Description |
|---|---|
| Data Models | Define structured data using Python classes |
| Type Validation | Validates values against declared types |
| Field Constraints | Enforces length, range, and other restrictions |
| Serialization | Converts model data into Python dictionaries or JSON |
| Error Reporting | Provides detailed validation errors |
| FastAPI Integration | Supports request validation and API documentation |

### Basic Model

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    salary: float
```

**Explanation:**

- `BaseModel` is the base class for Pydantic models.
- Each attribute defines an expected field and its type.
- Pydantic validates supplied data when creating a model instance.

---

## 3. Request Bodies in FastAPI

A **request body** contains data sent by the client to the server, commonly as JSON.

FastAPI uses Pydantic models to parse and validate request bodies.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    department: str
    salary: float

@app.post("/employees")
def create_employee(employee: Employee):
    return employee
```

### Example Request

```http
POST /employees
Content-Type: application/json
```

```json
{
  "name": "Rahul",
  "department": "IT",
  "salary": 60000
}
```

### Expected Response

```json
{
  "name": "Rahul",
  "department": "IT",
  "salary": 60000.0
}
```

**Key Point:** FastAPI automatically parses the JSON body and validates it against the `Employee` model.

---

## 4. Required, Optional & Default Fields

Pydantic fields can be required, nullable, or assigned default values.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    department: str
    salary: float
    email: str | None = None
    is_active: bool = True
```

| Field | Definition | Behavior |
|---|---|---|
| `name` | `str` | Required |
| `department` | `str` | Required |
| `salary` | `float` | Required |
| `email` | `str \| None = None` | Optional; defaults to `None` |
| `is_active` | `bool = True` | Optional; defaults to `True` |

**Important:** `str | None` permits `None`, but a default value is needed to make the field optional in the request.

---

## 5. Field Validation Using Field()

Pydantic's `Field()` defines validation constraints and field metadata.

```python
from pydantic import BaseModel, Field

class Employee(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    department: str = Field(min_length=2)
    salary: float = Field(gt=0)
    age: int = Field(ge=18, le=65)
```

### Common Constraints

| Constraint | Meaning |
|---|---|
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |
| `gt` | Greater than |
| `ge` | Greater than or equal to |
| `lt` | Less than |
| `le` | Less than or equal to |

### Example

```python
salary: float = Field(gt=0)
```

Accepts positive salary values and rejects zero or negative values.

---

## 6. Automatic Request Validation

FastAPI automatically validates request bodies against Pydantic models.

### Valid Request

```json
{
  "name": "Amit",
  "department": "HR",
  "salary": 50000,
  "age": 25
}
```

**Expected Status:** `200 OK` for an endpoint using the default success status.

### Invalid Request

```json
{
  "name": "A",
  "department": "HR",
  "salary": -5000,
  "age": 16
}
```

**Expected Status:** `422 Unprocessable Content`

### Common Validation Errors

| Error | Cause |
|---|---|
| Missing Field | Required field not provided |
| Invalid Type | Value cannot be validated as the declared type |
| Minimum Length | String shorter than permitted |
| Maximum Length | String longer than permitted |
| Range Violation | Numeric value outside allowed limits |

**Key Point:** FastAPI returns structured validation errors without requiring manual validation code for these constraints.

---

## 7. Response Models

A **response model** defines the structure of data returned by an API endpoint.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int):
    return {
        "id": employee_id,
        "name": "Amit",
        "department": "IT",
        "salary": 55000
    }
```

### Expected Response

```json
{
  "id": 101,
  "name": "Amit",
  "department": "IT"
}
```

**Explanation:**

- `response_model` validates and serializes response data.
- Fields not declared in the response model are excluded.
- Response models help maintain consistent API output.

---

## 8. Request Models vs Response Models

| Request Model | Response Model |
|---|---|
| Validates incoming data | Validates outgoing data |
| Defines accepted input fields | Defines returned output fields |
| Used as an endpoint parameter | Declared using `response_model` |
| Example: `EmployeeCreate` | Example: `EmployeeResponse` |

### Example

```python
class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: float

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
```

Separating request and response models provides better control over API input and output.

---

## 9. Today's Practical Assignment

**Project:** Employee Registration API

**Objective:** Extend the Day 03 Employee Information API by implementing employee registration with Pydantic validation.

### Requirements

- [ ] Create a FastAPI application.
- [ ] Define an `EmployeeCreate` model using `BaseModel`.
- [ ] Define an `EmployeeResponse` model.
- [ ] Add required employee fields.
- [ ] Add optional fields with default values.
- [ ] Apply validation constraints using `Field()`.
- [ ] Implement `POST /employees` to register employees.
- [ ] Generate a unique employee ID.
- [ ] Return `201 Created` for successful registration.
- [ ] Implement `GET /employees` to retrieve employees.
- [ ] Implement `GET /employees/{employee_id}`.
- [ ] Return `404 Not Found` for missing employees.
- [ ] Test valid and invalid request bodies using Postman.
- [ ] Verify automatic validation errors.
- [ ] Explore request and response schemas in Swagger UI.
- [ ] Capture screenshots and document the implementation.

**Data Storage:** In-memory Python dictionary.

**Constraint:** Focus on Pydantic models, POST requests, field validation, and response models. Database integration and advanced CRUD operations will be covered later.

---

## 10. Key Takeaways

- Pydantic provides structured data validation using Python type annotations.
- `BaseModel` defines reusable request and response schemas.
- FastAPI automatically parses JSON request bodies.
- `Field()` enforces validation constraints.
- Default values make model fields optional in requests.
- Invalid request data produces HTTP 422 validation errors.
- `response_model` controls the structure of API responses.
- Separating request and response models improves API design.

---

**Next Session:** Day 05 — CRUD Operations with FastAPI (POST, PUT, PATCH & DELETE).