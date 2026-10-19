# Day 03 — FastAPI Fundamentals & Basic Routing

**Date:** 19 October 2026 (Monday)  
**Learning Track:** Daily REST API & FastAPI Practice  
**Topic:** FastAPI Setup, ASGI, Routing & Automatic Documentation  
**Tools:** Python 3.12, PyCharm, FastAPI, Uvicorn, Postman  
**Level:** Beginner

---

## 1. Learning Objectives

- Understand FastAPI and its core features.
- Understand ASGI and the role of Uvicorn.
- Install and configure FastAPI.
- Create a basic FastAPI application.
- Implement GET endpoints using decorators.
- Understand path and query parameters.
- Explore automatic API documentation.
- Test endpoints using Postman.

---

## 2. Introduction to FastAPI

**FastAPI** is a modern Python web framework used to build REST APIs with Python type hints.

### Key Features

| Feature | Description |
|---|---|
| High Performance | Built on Starlette and Pydantic |
| Type Hints | Uses Python annotations for validation and documentation |
| Automatic Documentation | Generates Swagger UI and ReDoc |
| Data Validation | Uses Pydantic for request validation |
| Async Support | Supports `async def` and `def` endpoints |
| OpenAPI | Automatically generates an API specification |

### Basic Architecture

```text
Client (Postman / Browser)
          |
          v
      Uvicorn
     (ASGI Server)
          |
          v
       FastAPI
          |
          v
    Route Handler
          |
          v
     JSON Response
```

---

## 3. ASGI and Uvicorn

**ASGI (Asynchronous Server Gateway Interface)** is a standard interface between Python web applications and compatible servers.

**Uvicorn** is an ASGI server that runs FastAPI applications.

| Component | Responsibility |
|---|---|
| FastAPI | Defines routes and application logic |
| ASGI | Standardizes communication between server and application |
| Uvicorn | Receives HTTP requests and runs the ASGI application |

### Installation

```bash
pip install fastapi uvicorn
```

### Verify Installation

```bash
pip show fastapi
pip show uvicorn
```

---

## 4. Creating a FastAPI Application

**File:** `main.py`

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

### Explanation

| Component | Description |
|---|---|
| `FastAPI` | Main application class |
| `app = FastAPI()` | Creates the application instance |
| `@app.get("/")` | Registers a GET endpoint |
| `home()` | Function executed when the endpoint is requested |
| `return` | Returns data automatically serialized as JSON |

### Running the Application

```bash
uvicorn main:app --reload
```

- `main` — Python module (`main.py`).
- `app` — FastAPI application instance.
- `--reload` — Restarts the development server when source files change.

**Default URL:** `http://127.0.0.1:8000`

---

## 5. Basic Routing

A **route** connects an HTTP method and URL path to a Python function.

```python
@app.get("/")
def home():
    return {"message": "Home Page"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {"framework": "FastAPI", "day": 3}
```

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Health check |
| GET | `/info` | Application information |

---

## 6. Path Parameters

Path parameters identify specific resources through the URL.

```python
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {"employee_id": employee_id}
```

**Example Request:**

```http
GET /employees/101
```

**Response:**

```json
{
  "employee_id": 101
}
```

FastAPI automatically validates `employee_id` as an integer.

Invalid input produces a `422 Unprocessable Content` response.

---

## 7. Query Parameters

Query parameters provide optional filtering or configuration through the URL.

```python
@app.get("/employees")
def get_employees(department: str | None = None):
    return {"department": department}
```

**Example Request:**

```http
GET /employees?department=IT
```

**Response:**

```json
{
  "department": "IT"
}
```

### Path vs Query Parameters

| Path Parameter | Query Parameter |
|---|---|
| Part of URL path | Appears after `?` |
| Usually identifies a resource | Usually filters or configures results |
| Required unless route structure differs | Can be optional |
| `/employees/101` | `/employees?department=IT` |

---

## 8. Automatic API Documentation

FastAPI automatically generates interactive API documentation.

| Endpoint | Purpose |
|---|---|
| `/docs` | Swagger UI |
| `/redoc` | ReDoc documentation |
| `/openapi.json` | OpenAPI specification |

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows developers to inspect and execute API requests directly from the browser.

---

## 9. Today's Practical Assignment

**Project:** Employee Information API

**Objective:** Rebuild the basic GET functionality from previous sessions using FastAPI instead of `http.server`.

### Requirements

- [ ] Install FastAPI and Uvicorn.
- [ ] Create `main.py` with a FastAPI application.
- [ ] Implement `GET /` — welcome message.
- [ ] Implement `GET /health` — server health.
- [ ] Implement `GET /info` — application information.
- [ ] Implement `GET /employees` — retrieve all employees.
- [ ] Implement `GET /employees/{employee_id}` — retrieve an employee by ID.
- [ ] Add an optional `department` query parameter for filtering.
- [ ] Return `404 Not Found` for missing employee IDs.
- [ ] Test all endpoints using Postman.
- [ ] Explore `/docs` and `/redoc`.
- [ ] Capture screenshots and document the implementation.

**Data Storage:** In-memory Python dictionary.

**Constraint:** Focus on GET operations, routing, and parameter handling. POST, PUT, PATCH, DELETE, and Pydantic request models will be covered in subsequent sessions.

---

## 10. Key Takeaways

- FastAPI simplifies REST API development through decorators and type hints.
- Uvicorn runs FastAPI applications using ASGI.
- Routes map HTTP requests to Python functions.
- Path parameters identify resources.
- Query parameters support filtering.
- FastAPI automatically validates typed parameters.
- Swagger UI and ReDoc provide automatic API documentation.

---

**Next Session:** Day 04 — Pydantic Models, Request Bodies & Data Validation.