# Day 02 — REST Architecture & HTTP Methods

**Date:** 18 October 2026 (Sunday)  
**Learning Track:** Python Backend Development  
**Topic:** REST Architecture, HTTP Methods & Resource-Oriented API Design  
**Tools:** Python 3.12, PyCharm, Postman  
**Level:** Beginner

---

## Learning Objectives

- Understand REST architecture and its core principles.
- Identify resources and design RESTful endpoints.
- Understand GET, POST, PUT, PATCH, and DELETE.
- Differentiate safe and idempotent HTTP methods.
- Use appropriate HTTP status codes.
- Understand request bodies, headers, and JSON responses.

## 1. REST Architecture

**REST (Representational State Transfer)** is an architectural style for designing network-based applications.

A RESTful API exposes resources through URLs and uses standard HTTP methods to interact with them.

### Core REST Principles

| Principle | Description |
|---|---|
| Client–Server | Separates the client interface from server-side logic. |
| Statelessness | Each request contains the information needed to process it. |
| Cacheability | Responses indicate whether they can be cached. |
| Uniform Interface | Resources are accessed through consistent interfaces. |
| Layered System | Intermediaries can exist between client and server. |
| Code on Demand | Optional ability to transfer executable code to clients. |

## 2. Resources and Endpoints

A **resource** represents an entity such as an employee, product, or task.

An **endpoint** is a URL through which a client accesses a resource.

**Example: Employee Management API**

| Method | Endpoint | Operation |
|---|---|---|
| GET | `/employees` | Retrieve all employees |
| GET | `/employees/101` | Retrieve employee 101 |
| POST | `/employees` | Create an employee |
| PUT | `/employees/101` | Replace employee 101 |
| PATCH | `/employees/101` | Partially update employee 101 |
| DELETE | `/employees/101` | Delete employee 101 |

**Best Practices:**
- Use nouns instead of verbs in resource URLs.
- Prefer plural resource names.
- Use HTTP methods to indicate operations.
- Keep endpoint naming consistent.

## 3. HTTP Methods

| Method | Purpose | Request Body |
|---|---|---|
| GET | Retrieve a resource | Generally not used |
| POST | Create or process a resource | Usually |
| PUT | Replace a resource | Usually |
| PATCH | Partially modify a resource | Usually |
| DELETE | Remove a resource | Usually not required |

### PUT vs PATCH

**PUT:** Replaces the resource representation.

```json
{
  "name": "Rahul",
  "department": "IT",
  "salary": 60000
}
```

**PATCH:** Updates selected fields.

```json
{
  "salary": 65000
}
```

## 4. Safe and Idempotent Methods

**Safe Method:** Intended to retrieve information without modifying server state.

**Idempotent Method:** Repeating the same request produces the same intended effect on server state as executing it once.

| Method | Safe | Idempotent |
|---|---|---|
| GET | Yes | Yes |
| POST | No | Generally No |
| PUT | No | Yes |
| PATCH | No | Not Guaranteed |
| DELETE | No | Yes |

**Important:** An idempotent request may return different response codes when repeated, even though its intended effect remains the same.

## 5. HTTP Status Codes

| Code | Meaning | Typical Use |
|---|---|---|
| 200 | OK | Successful retrieval or update |
| 201 | Created | Resource successfully created |
| 204 | No Content | Successful deletion without response body |
| 400 | Bad Request | Invalid request data |
| 404 | Not Found | Requested resource does not exist |
| 405 | Method Not Allowed | HTTP method unsupported for the resource |
| 500 | Internal Server Error | Unexpected server-side failure |

## 6. HTTP Request and Response Structure

### Example POST Request

```http
POST /employees HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "name": "Rahul",
  "department": "IT"
}
```

### Example Response

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 101,
  "name": "Rahul",
  "department": "IT"
}
```

**Important Headers:**

| Header | Purpose |
|---|---|
| Content-Type | Identifies the format of the message body |
| Accept | Specifies preferred response media types |
| Authorization | Carries authentication credentials |
| Location | Identifies a newly created resource |

## 7. Today's Practical Assignment

**Project:** Employee REST API using Python's `http.server`.

**Implementation Requirements:**

- [ ] Create an in-memory employee data store.
- [ ] Implement GET endpoints.
- [ ] Implement POST to create employees.
- [ ] Implement PUT for complete replacement.
- [ ] Implement PATCH for partial updates.
- [ ] Implement DELETE to remove employees.
- [ ] Handle invalid requests and missing resources.
- [ ] Test API operations using Postman.
- [ ] Document implementation and test results.

## Day 02 Summary

Today's focus is understanding how RESTful APIs organize resources and use HTTP methods to perform operations.

**Key Takeaways:**
- REST is an architectural style, not a programming framework.
- HTTP methods define the intended operation on a resource.
- PUT and PATCH have different update semantics.
- Safe and idempotent are distinct HTTP properties.
- HTTP status codes communicate request outcomes.

**Next Session:** Day 03 — FastAPI Fundamentals, Application Setup, and Basic Routing.